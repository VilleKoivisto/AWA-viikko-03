"""
Simple script for getting all Python-repos from Github API
"""

import urllib.request
import json

def get_github_data():
    remote_url = "https://api.github.com/search/repositories?q=language:python"

    with urllib.request.urlopen(remote_url) as response:
        github_data = response.read()
        github_json = json.loads(github_data)

    return github_json


def print_data(python_thingies):
    get_forks = []

    for data_items in python_thingies["items"]:
        json_data = []

        id = data_items["id"]
        name = data_items["name"]
        fork_count = data_items["forks_count"]
        
        json_data.append(fork_count)
        json_data.append(id)
        json_data.append(name)

        get_forks.append(json_data)

    sorted_forks = sorted(get_forks, reverse=True)

    for item in sorted_forks:
        print(f"{item[0]}.{item[2]}.{item[1]}")


if __name__ == "__main__":
    print("All Python related repos in Github atm:")
    python_thingies = get_github_data()
    
    print_data(python_thingies)