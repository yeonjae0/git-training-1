arr = ['Fish', 'And', 'Chips']
N = len(arr)

for i in range(1<<N): #range(8)
	sub =[]
	# j: arr의 idx
	for j in range(N):
		#print(f'{j} {sub}')
		if i & (1 << j):
			sub.append(arr[j])
			#print(arr[j], end=' ')
	print(sub)
