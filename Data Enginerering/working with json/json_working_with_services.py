import json
import requests

url = 'https://finance.yahoo.com/'

try:
    r = requests.get(url)
    r.raise_for_status()
    #print(r)
    r_text = r.text
    #print(r_text)

    data = r.json()
    json_payload = json.dumps(data, indent = 4)

except requests.exceptions.HTTPError as e:
    print(f"HTTP error happened with : {e}")

except Exception as exp:
    print(exp)