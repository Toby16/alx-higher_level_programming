#!/usr/bin/python3
"""
Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = ""

    if len(sys.argv) > 1:
        q = sys.argv[1]
    data = {"q": q}

    r = requests.post(url, data=data)
    try:
        json_r = r.json()
        if json_r == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_r.get("id"), json_r.get("name")))
    except (TypeError, ValueError):
        print("Not a valid JSON")
