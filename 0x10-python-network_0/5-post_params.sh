#!/bin/bash
# a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -s -X POST "$1" -H "email: test@gmail.com" -H "subject: I will always be here for PLD" -d "param1=value1" -d "param2=value2"
