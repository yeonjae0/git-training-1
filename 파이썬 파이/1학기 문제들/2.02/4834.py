#cards

def my_max(x_list):
    maxV = 0
    for x in range(len(x_list)): #max구하기
        if x == 0: #첫번째 인덱스는 바로 max값
            maxV = x_list[0]
        elif x_list[x] > maxV: # 그 다음 값이 크면 바로 교체
            maxV = x_list[x]
    return maxV #x는 리스트

def my_index(y_list, y): #리스트와 리스트 내부의 값1
    id_list = []
    for z in range(len(y_list)):
        if y_list[z] == y:
            id_list.append(z)
    return my_max(id_list) #가장 큰 인덱스값 반환


T = int(input())

for a in range(T):
    N = int(input())
    nn = int(input())
    n_list = list(map(int, str(nn))) #이렇게 받는 리스트의 숫자는 int형
    cnt = [0] * 10
    for i in n_list:
        cnt[i] += 1 #cnt의 인덱스 값이 곧 n_list 내의 요소 값
    #print(cnt)

    print(f'#{a+1} {my_index(cnt,my_max(cnt))} {my_max(cnt)}')