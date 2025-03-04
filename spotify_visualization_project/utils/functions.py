"""
Constant functions to be used within the program
"""

import os
import pandas as pd

from pathlib import PosixPath
from dotenv import load_dotenv
from typing import List
from .constants import INTERMEDIATE_DIRECTORY, PROCESSED_DIRECTORY, REPO_ROOT

# NOTE: remove the DIRECTORY constants and take in the value for REPO ROOT / "data" / PROCESSED OR INTERMEDIATE


def load_environment_variables() -> List[str]:
    """
    Loads the environment variables and sets the AUTH_URL

    Inputs: None

    Returns:
        List of strings containing the following credentials:
            CLIENT_ID (str): client credentials for spotify web api
            CLIENT_SECRET (str): client credentials for spotify web api
    """
    load_dotenv("spotify_visualization_project/credentials/.env")

    CLIENT_ID = os.environ.get("CLIENT_ID")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

    return [CLIENT_ID, CLIENT_SECRET]


def create_directory(directory_path: PosixPath):
    """
    Checks if the directory path to the specified folder exists and creates it if necessary

    Inputs:
        directory_path (PosixPath): path to
    """
    if directory_path.exists():
        print("Directory already exists")
    else:
        directory_path.mkdir(parents=True, exist_ok=True)
        print(f"Created {directory_path}")


def output_data(folder_name: str, file_name: str, dataframe: pd.DataFrame):
    """
    Checks if the directory for the dataset is created and saves the data csv

    Inputs:
        folder_name: (str): Name of the folder to be created
        file_name (str): Name of the file
        dataframe (Pandas DataFrame): Pandas DataFrame to be outputted to the folder

    Returns: None, Saves the dataframe to the
    """
    directory_path = REPO_ROOT / "data" / folder_name

    create_directory(directory_path)

    dataframe.to_csv(directory_path / f"{file_name}.csv", index=False)

    print("🎶 Data Saved")
