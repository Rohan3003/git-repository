# Download mutiple files from the internet in parallel using Requests Library
from concurrent.futures import ThreadPoolExecutor
import requests

def download_file(url):
    ''' Download a file given an URL and save it to the current directory'''
    response = requests.get(url) # to send an HTTP GET request to the given URL and store it in respomse variable
    print(response)
    if "content-disposition" in response.headers:
        content_disposition = response.headers["content-disposition"]
        filename = response.headers["content-disposition"].split("filename=")[1]
    else:
        filename = url.split("/")[-1]
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"Downloaded {filename}")

# urls = [
#     "https://www.python.org/static/img/python-logo.png",    
#     "https://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv",
#     "https://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=xml"    
# ]
urls = ["https://www.python.org/"]

try:
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(download_file, urls)
except Exception as e:
    print(e)
