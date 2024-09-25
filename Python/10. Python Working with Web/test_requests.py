import requests
url = input(str("Enter the url :")) # https://www.google.com
response = requests.get(url)
print(response.text)