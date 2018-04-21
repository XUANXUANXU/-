list = []
def register():
	flag = 0
	account = input("请输入账号")
	for i in list:
		if account == i["account"]:
			flag = 1
			print("该账号已经被注册过了")
			break
	if flag == 0:
		pwd = input("请输入密码")
		dict = {}
		dict["account"] = account
		dict["pwd"] = pwd
		list.append(dict)
		print("注册成功")

def login():
	account = input("请输入账号")
	pwd = input("请输入密码")
	flag = 0
	for i in list:
		if account == i['account']:
			if i.get("status") == 1:
				print("账号正在登陆着")
			else:
				if pwd == i["pwd"]:
					print("登陆成功")




def out():
	pass




while True:
	fun = int(input("请选择功能: 1:注册 2:登录 3:登出"))
	if fun == 1:
		register()
	elif fun == 2:
		login()
	elif fun == 3:
		out()
	else:
		print("退出系统")
		break
