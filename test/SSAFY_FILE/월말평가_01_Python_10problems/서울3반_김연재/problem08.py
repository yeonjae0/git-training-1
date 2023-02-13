# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    result = ''
    num = 0
    upper_list = list(map(int, range(65, 91)))
    lower_list = list(map(int, range(97, 123)))
    for i in word: # i는 개별 알파벳 ex. apple의 a
        if i.islower() == True:
            for a in range(len(lower_list)): #a는 소문자 아스키 번호 리스트의 인덱스 번호
                if ord(i) == lower_list[a]:
                    num = a + n #인덱스 번호에 n 더하기
                    
                    if num > len(lower_list)-1:
                        result += chr(lower_list[num-len(lower_list)])
                    else:
                        result += chr(lower_list[num])

        elif i.isupper() == True:
            for A in range(len(upper_list)):
                if ord(i) == upper_list[A]:
                    num = A + n
                    
                    if num > len(upper_list)-1:
                        result += chr(upper_list[num-len(upper_list)])
                    else:
                        result += chr(upper_list[num])
    return result


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(caesar('apple', 5))      # fuuqj
    print(caesar('ssafy', 1))      # ttbgz
    print(caesar('Python', 10))    # Zidryx
