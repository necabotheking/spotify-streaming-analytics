# MySpotiPY - Spotify Streaming Analytics 

**A pipeline that visualizes my spotify steaming analytics**


## Table of Contents: 
- Summary
- Technologies/Project Prerequisites
- Project Structure
- Poetry Commands
- Status
- Reflection


## Summary
This project creates a dynamic dashboard using [my](github.com/necabotheking) extended Spotify streaming data from 2018 to 2023.

Note: The Spotify Web API depreciated some of the key endpoints needed for analyzing the song data

## Technologies/Project Prerequisites 
- Python
- Pyenv
- Spotify Streaming Data History
- Spotify Web API (Spotify for Developers) 
    A CLIENT_ID and CLIENT_SECRET are necessary, which are stored in variables
    of the same name.
    The developer of this project has stored the API key in a .env files which are included in the .gitignore 

## Project Structure

- `spotify_visualization_project`
    - `api`
    - `credentials`
    - `data`
        - `raw`
        - `intermediate`
        - `processed`
    - `data_handling`
    - `ml`
    - `tests`
    - `utils`
    - `visualization`
- `__main__.py`
- `requirements.txt`


## Status
In-Progress

## Reflection
TBF