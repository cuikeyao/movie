import requests
import json
import os

username = os.environ.get('username')
password = os.environ.get('password')
token_url = os.environ.get('token_url')
addr_url = os.environ.get('addr_url')

body = '''{"email":"%s","password":"%s"}''' % (username, password);

token_response = requests.post(token_url, data=body)

token_response_dict = json.loads(token_response.text)

token = token_response_dict["data"]["token"]

headers_str = '''{"Authorization":"Bearer %s"}''' % token

headers = json.loads(headers_str)

addr_response = requests.get(addr_url, headers=headers)

addr_response_dict = json.loads(addr_response.text)

addr = addr_response_dict["data"]["items"][1]["public_url"]

script = '''<script type="text/javascript">window.location.href = "%s";</script>''' % addr

with open("index.html", "w") as file:
    file.write(script)
