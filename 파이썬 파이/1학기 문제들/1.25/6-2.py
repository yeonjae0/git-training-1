grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
lst = []
max_price = 0
grain = ''

for i in grain_lst: # i는 개별 튜플
    for j in i:
        lst.append(j) #lst = ['고구마', 3000, '감자', 2000, '옥수수', 4500, '토란', 1300]
for x in range(1, len(lst)+1, 2):
    if x == 1:
        max_price = lst[1]
        grain = lst[0]
    elif lst[x] > max_price:
        max_price = lst[x]
        grain = lst[x-1]
print(grain)

