#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    this_page = response.read()

print("Body response:")
print("    - type:", type(this_page))
print("    - content:", this_page)
print("    - utf8 content:", this_page.decode("utf-8"))
