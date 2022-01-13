import requests
import pprint

r = requests.get('https://api.themoviedb.org/3/movie/550?api_key=5f96ca821b0df5fb5a9314d566a5e5ab')
pprint.pprint(r.json()['genres'][0])