import requests
from pprint import pprint


def recommendation(title):
    URL = 'https://api.themoviedb.org/3/search/movie?api_key=40a69d93e84171e666e3a8b8cfd8acb4&language=ko-KR&page=1&include_adult=false'

    params = {
    'api_key': '40a69d93e84171e666e3a8b8cfd8acb4',
    'language': 'ko-KR',
    'region' : 'KR',
    'query': title 
    }
    response = requests.get(URL, params=params).json()
    n_list =  response['results'] #n_list는 리스트 안 개별 딕셔너리
    ans = []
    
#검색할 수 없는 영화는 빈 리스트. 아래 i_d를 만나면 오류가 나기 때문에 그 전에
#빈 리스트는 리턴 None값 반환
    if not n_list:
        return None 

    i_d = n_list[0]["id"]
    URL_ = f'https://api.themoviedb.org/3/movie/{i_d}/recommendations'
    params_ = {
    'api_key': '40a69d93e84171e666e3a8b8cfd8acb4',
    'language': 'ko-KR',
        'region' : 'KR',
        'query': title 
        # 'movie_id': n_list[i]["original_title"] 있어도 없어도 ㄱㅊ
    }

    response_ = requests.get(URL_, params=params_).json()
    for i in range(len(response_["results"])):
        ans.append(response_["results"][i]["title"])

    if not title:
        return []

    return ans






# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
