import xmltodict
import json
import requests

url = "https://www.baeldung.com/junit-5-runwith"

headers = {
  'Content-Type': 'application/xml'
}

response = requests.request("GET", url, headers=headers, data = None)

print(xmltodict.parse(response.text.encode('utf8')))