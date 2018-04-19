def jisuanqi(x,y,fuhao):
	if fuhao == "+":
		z = x+y
		print("和是%0.2f"%z)
	elif fuhao == "-":
		z = x-y
		print("差是%0.2f"%z)
	elif fuhao == "*":
		z = x*y
		print("乘是%0.2f"%z)
	elif fuhao == "/":
		if y !=0:
			z = x/y
			print("除是%0.2f"%z)
		else:
			print("输入有误")
while True:
	x = float(input("请输入一个数字"))
	y = float(input("请再输入一个数字"))
	z = input("请输入+-*/")
	jisuanqi(x,y,z)
