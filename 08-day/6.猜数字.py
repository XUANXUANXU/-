import random
a = random.randint(1,100) 
i = 1
while i <= 10:
	b = int(input("请输入数字"))
	if a > b:
		print("猜小了")
	elif a < b:
		print("猜大了")
	else:
		print("猜对了")
		break
	
	print("猜了%d次"%i)
	i+=1
