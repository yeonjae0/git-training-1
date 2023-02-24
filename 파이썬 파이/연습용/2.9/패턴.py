#T: Target // P:Pattern
#lps longest prefix suffix

def pre_process(p):
    lps = [0] * len(p)

    #lps를 만들기 위해 패턴 인덱스
    j = 0

    #처음부터 끝까지 순회
    for i in range(1, len(p)):
        #패턴 발견 해당 인덱스에 있는 char가 똑같다면
        if p[i] == p[j]:
            lps[i] = j+ 1
            j += 1

        #다르다면 j인덱스를 초기화 -> Pattern의 가장 처음부터 다시 인식하도록 
        else:
            j = 0
            if p[i] == p[j]:
                lps[i] = j+1
                j += 1
    return lps

p = 'abcdabcdef'

rlt = pre_process(p)
print(rlt)