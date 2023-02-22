import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')

# 1. left & right & parent 배열을 따로 선언해서 받기

# 2. left, right, parent 미리 초기화를 해놓고 사용하기
#  1             2        3
# [[0, 0, 0], [2, 3, 0], []]

# 1. left & right & parent 배열을 따로 선언해서 받기

def pre_order(n):
    if n > 0:
        print(n, end=' ')
        # cnt += 1
        pre_order(left[n])
        pre_order(right[n])

def in_order(n):
    if n != 0:
        in_order(tree[n][0])
        print(n, end=' ')
        in_order(tree[n][1])
        pass

def post_order(n):
    if n != 0:
        in_order(tree[n][0])
        in_order(tree[n][1])
        print(n, end=' ')  # 특정 로직을 수행하는 곳

V = int(input())  # V = 13
E = V - 1  # 간선은 노드보다 하나 적게  # E = 12
edge = list(map(int, input().split()))

left = [0] * (V + 1)  # 부모의 인덱스로 왼쪽 자식 번호 저장
right = [0] * (V + 1)  # 부모의 인덱스로 오른쪽 자식 번호 저장
parent = [0] * (V + 1)  # 자식을 인덱스로 부모 번호 저장

root = 0  # 루트 번호부터 시작

for i in range(E):
    p1, c1 = edge[i * 2], edge[i * 2 + 1]  # 부모, 자식

    if left[p1] == 0:  # 왼쪽 자식이 없다면
        left[p1] = c1  # 부모의 인덱스로 자식 번호 저장
    else:  # 왼쪽 자식이 없다면
        right[p1] = c1  # 부모의 인덱스로 자식 번호 저장
    parent[c1] = p1  # 자식을 인덱스로 부모를 저장

for i in range(1, V + 1):
    if not parent[i]:
        root = i
        break


# 2. left, right, parent // 아래와 같은 형태로 연결 정보 기록하기
#  1             2        3
# [[0, 0, 0], [2, 3, 0], []]


'''
2번 노드
- 왼쪽: 2번
- 오른쪽: 3번
-부모: X
'''

tree = [[0 for _ in range(3)] for _ in range(V + 1)]  # tree = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]...]

for i in range(E):
    parent, child = edge[i * 2], edge[i * 2 + 1]

    #[0, 0, 0] 0번째: 왼쪽 자식 / 1번째: 오른쪽 자식/ 2번쨰: 부모노드
    if not tree[parent][0]:  #falsy 참조. # parent 노드의 왼쪽 자식이 없다면, 왼쪽 자식 넣고
        tree[parent][0] = child

    else:  # 왼쪽 자식이 있고, 오른쪽 자식이 없다면, 오른쪽 자식 넣고
        tree[parent][1] = child
    tree[child][2] = parent
    print(tree)
