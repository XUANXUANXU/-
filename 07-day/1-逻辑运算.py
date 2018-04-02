hight = float(input("请输入身高"))
money = float(input("请输入身价"))
nice = float(input("请输入颜值分"))

if hight >= 180 and money > 2000000 and nice > 90:
	print("帅气又多金")

elif hight > 180 and money < 2000000 and nice > 90:
	print("又高又帅的小哥哥")

elif hight < 180 and money > 2000000 and nice < 90:
	print("只会炫耀钱的土豪")

elif hight > 180 and money < 2000000 and nice < 90:
	print("傻大个")
else:
	print("可以回炉重造了")
