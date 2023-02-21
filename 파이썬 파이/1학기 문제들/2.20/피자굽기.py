import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())  # n: 화덕 크기, m: 피자 개수
    pizza = list(map(int, input().split()))

    lst = []  # 화덕

    pizza_lst = [[pizza[x], x+1] for x in range(m)]  # [치즈양, 피자 순서]
    for y in range(n):  # 화덕에 피자들을 먼저 넣어주고 시작
        if not pizza_lst:  # 화덕 크기가 피자 개수보다 클 경우
            break
        else:
            lst.append(pizza_lst.pop(0))


    while len(lst) != 1:
        lst[0][0] = lst[0][0] // 2
        if lst[0][0] != 0:
            lst.append(lst.pop(0))
        else:  # 0이 되었을 경우
            if not pizza_lst:  # 피자 리스트에 원소가 없으면
                lst.pop(0)
            else:  # 피자 리스트에 원소가 있으면
                lst.pop(0)
                lst.append(pizza_lst.pop(0))
    print(f'#{t} {lst[0][1]}')

    # while len(lst) != 1:
    #     i += 1
    #     i = i % len(lst)
    #     lst[i][0] //= 2
    #     if lst[i][0] == 0 and pizza_lst:
    #         lst[i] = pizza_lst[0]
    #         pizza_lst.pop(0)
    #     elif (lst[i][0] == 0) and not pizza_lst:
    #         lst.pop(i)
    # print(lst)

