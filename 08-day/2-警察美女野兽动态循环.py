'''
1:警察
2:小偷
3:美女
'''
a = int(input("请输入次数"))
b = 1
import random
while b <= a:
	
	computer = random.randint(1,3)
	xuan = int(input("请输入1:警察 2:小偷 3:美女"))

	if (xuan == 1 and computer == 2) or (xuan == 2 and computer == 3) or (xuan == 3 and computer == 1):
		print("轩轩赢啦")
	elif xuan == computer:
		print("平局")
	else:
		print("电脑赢啦")
	b+=1
