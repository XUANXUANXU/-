def sushu(x,y):
	for i in range(x,y+1):
		n = 0
		for j in range (2,i):
			if i%j == 0:
				n=1
				break
		if n == 0:
			print(i)
sushu(100,200)		
