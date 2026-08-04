"""
Author: Lane Dorscher
Date: 08/04/2026
Course: CSD-325
Assignment: 9.2
Description: Simple program connects to a public testing API for users.
             Prints both the unformatted and formatted json response to the console.
"""

import requests
import json

## Constants
API = "https://jsonplaceholder.typicode.com/users"

## Functions
def main():
    try:
        response = requests.get(API)
        print(f"Connection Status: {response.status_code}")

        if response.status_code == 200:
            print("Connection successful!")

            print("\n----- Unformatted JSON -----")
            print(response.json())

            print("\n----- Formatted JSON -----")
            jprint(response.json())
        else:
            print("Unable to retrieve data from the API.")

    except requests.exceptions.RequestException as e:
        print(f"Connection failed: {e}")

def jprint(jobj):
    '''Pretty print the JSON object'''
    text = json.dumps(jobj, sort_keys=True, indent=4)
    print(text)

## Program entry
if __name__ == "__main__":
    main()

