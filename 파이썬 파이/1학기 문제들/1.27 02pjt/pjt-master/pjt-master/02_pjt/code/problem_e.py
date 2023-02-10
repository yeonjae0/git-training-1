import requests
from pprint import pprint


def credits(title):
    URL = 'https://api.themoviedb.org/3/search/movie'

    params = {
    'api_key': '40a69d93e84171e666e3a8b8cfd8acb4',
    'language': 'ko-KR',
    'region' : 'KR',
    'query': title 
    }
    response = requests.get(URL, params=params).json()
    n_list =  response['results'] #n_list는 리스트 안 개별 딕셔너리

    cast = []
    crew = []
    if not n_list: # 에러 생기기 전에 빈리스트 None값
        return None
    i_d = n_list[0]["id"]
    URL_ = f'https://api.themoviedb.org/3/movie/{i_d}/credits'
    params_ = {
    'api_key': '40a69d93e84171e666e3a8b8cfd8acb4',
    'language': 'ko-KR',
        'region' : 'KR',
        'query': title 
        # 'movie_id': n_list[i]["original_title"] 있어도 없어도 ㄱㅊ
    }

    response_ = requests.get(URL_, params=params_).json()
    #response_.keys()보면 dict_keys(['id', 'cast', 'crew']) 길어서 그냥 response_로는 확인 어려움
    for i in range(len(response_['cast'])): 
        if response_['cast'][i]['cast_id'] < 10:
            cast.append(response_["cast"][i]['name'])
    for j in range(len(response_['crew'])):
        if response_['crew'][j]['department'] == "Directing":
            crew.append(response_["crew"][i]['name'])


    # 결과가 길어서 잘릴 수 있음.
    #return response_.keys()
    return {'cast': cast, 'directing' : crew}


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
