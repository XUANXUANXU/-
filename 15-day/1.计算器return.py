def jisuanqi(x,y,fuhao):
	if fuhao == "+":
		z = x+y
 		return z
	elif fuhao == "-":
		z = x-y
		return z    
	elif fuhao == "*":
		z = x*y
		return z
	elif fuhao == "/":
		if y !=0:
			z = x/y
			return z
		else:
			"输入有误"
	while True:
		x = float(input("请输入一个数字"))
		y = float(input("请再输入一个数字"))
		z = input("请输入+-*/")
	    d = jisuanqi(x,y,z)
		print(d)
