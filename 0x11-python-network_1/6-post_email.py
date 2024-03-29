#!/usr/bin/python3
"""
This Python Script takes in a URL and Sends a POST request to a given URL
with a given email and displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}

    req = requests.post(url, data=value)
    print(req.text)
