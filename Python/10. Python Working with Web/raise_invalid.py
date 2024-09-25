import requests
from requests.exceptions import HTTPError
 
URLS = ["https://api.github.com", "https://api.github.com/invalid"]

for url in URLS:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occured with {http_err}")
    except Exception as e:
        print(f"Other error occured {e}")
    else:
        print("Success")