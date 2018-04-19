def biao(x,y):
	for i in range(x,y):
		for j in range (x,i+1):
			print("%d*%d=%d\t"%(j,i,j*i),end="")
		print("")
biao(1,10)
