#노란블럭 Flatten
def my_max(x_list):
    maxV = 0
    for x in range(len(x_list)): #max구하기
        if x == 0: #첫번째 인덱스는 바로 max값
            maxV = x_list[0]
        elif x_list[x] > maxV: # 그 다음 값이 크면 바로 교체
            maxV = x_list[x]
    return maxV

def my_min(y_list):
    minV = 0
    for y in range(len(y_list)): #min구하기
        if y == 0: #첫번째 인덱스는 바로 min값
            minV = y_list[0]
        elif y_list[y] < minV: # 그 다음 값이 작으면 바로 교체
            minV = y_list[y]
    return minV

def my_index(z_list, z): #리스트와 리스트 내부의 값1 넣어서 인덱스 반환
    for q in range(len(z_list)):
        if z_list[q] == z:
            return q

for a in range(10):
    N = int(input())
    n_list = list(map(int, input().split()))
    for b in range(N): #옮기는 횟수 만큼
        n_list[my_index(n_list,my_max(n_list))] -= 1 #리스트 맥스값의 인덱스를 받아서 최대값인 리스트[인덱스] 값 -1 해주기
        n_list[my_index(n_list,my_min(n_list))] += 1
    print(f'#{a+1} {max(n_list)- min(n_list)}')
