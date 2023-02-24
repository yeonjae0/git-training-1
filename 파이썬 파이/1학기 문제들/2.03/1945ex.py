#N = 50 = 2 * 5 * 5 나눠서 떨어지면
#while N % 5 == 0
# cnt - 5 += 1 
#    N = N//5
# for i(0, len(divs)):
#     while


divs =[2, 3, 5, 7, 11]


# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cnts = [0] * len(divs)

    for i in range(len(divs)):
        while N % divs[i] == 0:
            cnts[i] += 1
            N = N//divs[i]



    print(f"#{test_case}", *cnts)