
import random
a = random.randint(1,100)
for i in range (1,11):

	b = int(input("请输入一个数字(1到100):"))
	if a > b:
		print("猜小了")
	elif a < b:
		print("猜大了")
	else:
		print("猜中")
		break
	print("猜了%d次"%i)
