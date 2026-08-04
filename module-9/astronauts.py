"""
Author: Lane Dorscher
Date: 08/04/2026
Course: CSD-325
Assignment: 9.2
Description: Simple program to get and format json response from web API
"""

import requests
import json

API = 'http://api.open-notify.org/astros.json'

def main():
    response = requests.get(API)
    print(response.status_code)
    jprint(response.json())

def jprint(jobj):
    text = json.dumps(jobj, sort_keys=True, indent=4)
    print(text)



if __name__ == '__main__':
    main()