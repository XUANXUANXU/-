a = "123456"
p = "000000"
print("TIMI")
login = input("请选择登陆方式 1=qq 2=微信 3=账号登录") 
if login == "1":
	print("qq登陆成功")
	choose_hero = int(input("请选择英雄 1=肉 2=法师 3=射手 4=刺客 5=辅助"))
	if choose_hero == 1:
		print("为王者的信念连睡觉也穿着铠甲")
	elif choose_hero == 2:
		print("请尽情吩咐妲己主人")
	elif choose_hero == 3:
		print("鲁班大师智商二百五")
	elif choose_hero == 4:
		print("今朝有酒今朝醉来干")
	elif choose_hero == 5:
		print("男神是孟德大人喜欢宠物是阿典梦想是养只羊驼")

elif login == "2":
	print("微信登录成功")
elif login == "3":
	account = input("请输入账号")
	pwd = input("请输入密码")
	if account == a and pwd == p:
		print("显示登陆成功")
	else:
		print("登录失败")
