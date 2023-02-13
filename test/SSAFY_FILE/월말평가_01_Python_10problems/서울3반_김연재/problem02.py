# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# python 내장함수 min, max 사용 금지
def min_max(scores):
    result_min = 0
    result_max = 0
    for i in range(len(scores)): 
        if i == 0:
            result_max = scores[0]
        elif scores[i] > result_max: #새로운 값이 기존의 값을 비교
            result_max = scores[i] # 대체
    
    for j in range(len(scores)):
        if j == 0:
            result_min = scores[0]
        elif scores[j] < result_min:
            result_min = scores[j]
    return (result_min, result_max)


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(min_max(scores))    # (75, 90)
