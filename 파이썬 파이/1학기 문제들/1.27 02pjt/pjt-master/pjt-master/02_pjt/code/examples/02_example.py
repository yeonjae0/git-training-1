# requests 사용 예시 2

import requests


URL = 'https://api.themoviedb.org/3/movie/popular'

params = {
    'api_key': '40a69d93e84171e666e3a8b8cfd8acb4',
    'language': 'ko-KR',
    'region' : 'KR'
    #'name': 'michael',
    #'country_id': 'KR',
}

response = requests.get(URL, params=params).json()
#print(response)

print(response['results'][0]['vote_average'])

