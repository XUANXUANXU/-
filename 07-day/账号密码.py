account = input("请输入账号")
pwd = input("请输入密码")

if account == "123456" and pwd == "abc":
	print("登陆成功")
elif account != "123456":
	print("账号错误")
elif pwd != "abc":
	print("密码错误")
