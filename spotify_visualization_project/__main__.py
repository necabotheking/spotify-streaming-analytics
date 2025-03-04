"""
Main function for the Spotify Web API Project
"""

import argparse

import spotify_visualization_project.api.spotify_web_api
import spotify_visualization_project.data_handling.spotify_streaming_data  # import run_data_handling
import spotify_visualization_project.api  # .spotify_web_api #import run_api

# import spotify_visualization_project.data_handling.streaming_to_excel #import main


def main():
    """
    This function runs the project, outputting the intermediate version of the dataframe after data_handling
        - Creating a streaming and genre dataframe with the API module
        - Creating
    """
    # TODO: ADD ARGPARSER FOR COMMANDS THAT WILL CREATE THE PROJECT,
    # RUN DATA_HANDLING
    # RUN API
    # pass
    # BUG: Figure out a way to run the package as the below
    # FIX: The fucking function wasn;t named MAIN
    # NOTE: RENAME THE MAIN FUNCTIONS WITHIN EACH MODULE TO MAIN

    spotify_visualization_project.data_handling.spotify_streaming_data.run_data_handling()
    print("Streaming Dataframe outputted 🎶!")

    # streaming_dataframe, genre_dataframe = run_api(streaming_dataframe)
    spotify_visualization_project.api.spotify_web_api.run_api()
    # main(streaming_dataframe, genre_dataframe)


if __name__ == "__main__":
    main()
