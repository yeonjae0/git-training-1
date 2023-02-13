# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def calc_lunch_cost(lunch_cost):
    result = 0
    for i in lunch_cost:  #i에 key 값이 차례로 들어간다.
        result += lunch_cost[i] #result에 키값에 해당하는 value값이 차례로 더해진다.
    return result



# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    lunch_cost = {
        '이싸피' : 12000,
        '김싸피' : 30000,
        '박싸피' : 10000,
        '최싸피' : 15000,
        '조싸피' : 18000, 
    }

    print(calc_lunch_cost(lunch_cost))  # 85000