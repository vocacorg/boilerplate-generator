import requests
import sys
import os
import base64
import json

if len(sys.argv) < 3:
    print("Required arguments are missing")
    quit()

repository_name = sys.argv[1]
repository_desc = sys.argv[2]

data = {"name": repository_name,
        "description": repository_desc,
        "homepage": 'https://github.com',
        "private": False}

headers = {'Accept': 'application/vnd.github.baptiste-preview+json'}
repository_url = "https://api.github.com/orgs/vocacorg/repos"
resp = requests.post(repository_url, data=json.dumps(data), headers=headers, auth=('fdsfds', 'fdsfds'))

if resp.status_code != 201:
    response = resp.json()
    print("Error occurred:", response['errors'][0]["message"])
