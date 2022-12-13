import requests

URL = "https://meowfacts.herokuapp.com/"

result = requests.get(URL)

data = result.json()

print(data)
