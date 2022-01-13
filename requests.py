import requests

url = "https://imdb8.p.rapidapi.com/auto-complete"

querystring = {"q":"game of thr"}

headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "6e90e3efd1mshd899e572e1ea22cp195093jsndead40db2b01"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)