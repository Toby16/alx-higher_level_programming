#!/bin/bash
# a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -X GET -s -w "%{http_code}" "$1" -o /dev/null | grep -q 200 && curl -s "$1"
