import os
import pandas as pd
from typing import List
from datetime import date

from pathlib import Path

from spotify_visualization_project.utils.constants import (
    DATA_DIRECTORY,
    INTERMEDIATE_DIRECTORY,
)
from spotify_visualization_project.utils.functions import output_data


def read_all_streaming_history() -> dict:
    """
    Navigates to the data folder and creates lists of files by year to be read in

    Inputs: None

    Returns: all_streaming_history: dictionary of Pandas DataFames with year of spotify data as the key
    """
    # TODO: replace this with a value that auto detects the current year based on user input in the terminal
    current_year = date.today().year
    year_lst = [*range(2018, 2024)]

    streaming_dict = {}

    for year in year_lst:
        year_files = [
            os.path.join(DATA_DIRECTORY, file)
            for file in os.listdir(DATA_DIRECTORY)
            if str(year) in file
        ]
        formatted_dataframe = read_spotify_data(year_files)
        streaming_dict[year] = formatted_dataframe

    all_streaming_history = pd.concat(streaming_dict.values(), axis=0)


    return all_streaming_history


def read_spotify_data(year_files: List[str]) -> pd.DataFrame:
    """
    Reads the data into a pandas dataframe and concatenates years into the one Pandas DataFrame

    Inputs:
        year_files (lst): List of strings of json files of spotify streaming data

    Returns: streaming_df: Pandas Dataframe of concatenated data from one year of spotify streaming data
    """
    streaming_lst = []

    for file in year_files:
        df = pd.read_json(file)
        formatted_df = format_dataframe(df)
        streaming_lst.append(formatted_df)
    streaming_df = pd.concat(streaming_lst, axis=0)

    return streaming_df


def format_dataframe(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Returns the Pandas DataFrame formatted in-place

    Inputs:
            dataframe: unformatted dataframe of spotify streaming data

    Returns: dataframe: formatted dataframe of spotify streaming data
    """

    dataframe["uniqueID"] = (
        dataframe["master_metadata_album_artist_name"]
        + " : "
        + dataframe["master_metadata_track_name"]
    )

    dataframe = dataframe[~(dataframe['episode_show_name'].notna() & dataframe['spotify_episode_uri'].notna())]

    #print(dataframe["spotify_episode_uri"].isna())

    # drop unnecessary columns containing identifying information
    dataframe = dataframe.drop(
        [
            "user_agent_decrypted",
            "ip_addr_decrypted",
            "episode_name",
            "episode_show_name",
            "spotify_episode_uri",
            "username",
            "platform",
            "conn_country",
            "offline",
        ],
        axis=1,
    )

    uri = dataframe["spotify_track_uri"].str.split(":", expand=True)

    dataframe["spotify_uri_clean"] = uri[2]

    dataframe = dataframe.dropna(subset=["spotify_track_uri"])


    return dataframe


# TODO: MOVE THIS FUNCTION TO THE UTILS SECTION
def create_directory():
    """
    Checks if the intermediate data folder exists
    """
    if INTERMEDIATE_DIRECTORY.exists():
        print("Directory already exists")
    else:
        INTERMEDIATE_DIRECTORY.mkdir(parents=True, exist_ok=True)
        print(f"Created {INTERMEDIATE_DIRECTORY}")


def save_intermediate_data(streaming_df: pd.DataFrame):
    """
    saves the intermediate data
    """
    create_directory()
    streaming_df.to_csv(
        INTERMEDIATE_DIRECTORY / "spotify_streaming_data.csv", index=False
    )

    print("Cleaned Streaming Data Saved")


def run_data_handling():
    """
    Runs the main functions and returns the 2018 - 2023 steaming dataframe

    Inputs: None

    Returns: yearly_streaming_dict (dict)
             all_streaming_history_dict (Pandas Frame)
    """
    all_streaming_history_dict = read_all_streaming_history()

    output_data("intermediate", "spotify_streaming_data", all_streaming_history_dict)


if __name__ == "__main__":
    run_data_handling()
