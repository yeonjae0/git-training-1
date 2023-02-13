# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# 반드시 재귀함수로 구현해야 합니다.
def dec_to_bin(number):
    n = ''
    if number <= 1: #여기서 멈추기
        return str(number)
    elif number > 1:
        n += str(number % 2)
        return dec_to_bin(number // 2) + str(n) 

#풀이 (옆반?)
# def recursion(n):
#     if n//2==0:
#         return str(n)
#     return recursion(n//2) + str(n%2)

# print(recursion(10))

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(dec_to_bin(10))  # 1010
    print(dec_to_bin(5))   # 101
    print(dec_to_bin(50))  # 110010
