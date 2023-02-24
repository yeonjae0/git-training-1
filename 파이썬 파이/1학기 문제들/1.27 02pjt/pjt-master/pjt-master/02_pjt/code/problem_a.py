import requests


def popular_count():
    URL = 'https://api.themoviedb.org/3/movie/popular'

    params = {
    'api_key': '40a69d93e84171e666e3a8b8cfd8acb4',
    'language': 'ko-KR',
    'region' : 'KR'

    }  
    response = requests.get(URL, params=params).json()
    ans = 0

    for i in range(len(response['results'])): #i가 개별 딕셔너리 (count쓰면 더 편할지도)
        ans += 1 
    return ans



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
