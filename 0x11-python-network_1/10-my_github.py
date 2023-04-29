#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials
(username and password)
and uses the GitHub API to display your id
"""

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"

    auth = requests.auth.HTTPBasicAuth(username, password)
    response = requests.get(url, auth=auth)

    user_data = response.json()
    user_id = user_data.get("id")
    print(user_id)
