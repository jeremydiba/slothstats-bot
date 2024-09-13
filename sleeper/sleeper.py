import requests
import json

def get_nfl_state():
    url = "https://api.sleeper.app/v1/state/nfl"
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code != 200:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

    # Parse JSON into Python object
    nfl_state = json.loads(response.text)

    return nfl_state

def get_league_rosters(league_id):
    url = f'https://api.sleeper.app/v1/league/{league_id}/rosters'
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code != 200:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

    # Parse JSON into Python object
    rosters = json.loads(response.text)

    return rosters