for i in range (2,101):
	n = 0
	for j in range (2,i):
		if i%j == 0:
			n=1
	if n == 0:
		print(i)
