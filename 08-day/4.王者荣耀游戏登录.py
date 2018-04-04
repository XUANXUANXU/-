a = "小可爱"
p = "123456"
d = 1#输入次数
while True:
	account = input("请输入游戏名")
	pwd = input("请输入密码")
	
	if account == a and pwd == p:
		print("登陆成功")
		choose_hero = int(input("请选择英雄 0=ADC 1=肉 2=法师"))
		if choose_hero == 0:
			print("鲁班大师")
		elif choose_hero == 1:
			print("程咬金")
		elif choose_hero == 2:
			print("王昭君")
		break
	else:
		
		print("错误%d次"%d)
		d+=1
		if d == 4:
			print("账号被封")
			break
