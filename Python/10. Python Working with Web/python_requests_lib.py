import requests
url = 'https://api.github.com' # github REST API

# GET method
response = requests.get(url)
print(response)

# Status code
print(response.status_code)

# Test reponse
if response.status_code == 200:
    print("Success!")
elif response.status_code == 404:
    print("Not Found.")

# Refactoring above code
if response:
    print("Success!")
else:
    raise Exception(f"Non-success with status code: {response.status_code}")


# for more details go to - raise_invalid.py 

# CONTENT - response.content gives you raw bytes of the response
print(response.content)
print(type(response.content))

# CONTENT - text response
print(response.text)
print(type(response.text))

print(response.json())