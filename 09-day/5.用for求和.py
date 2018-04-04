
while True:
	i = int(input("请输入一个数字:"))
	s = int(input("请再输入一个数字:"))


	if i < s:
		k = 0
		for a in range(i,s):
			k+=a
			print(k)
		break
			
	else:
		print("输入错误")
	 		
		
	

