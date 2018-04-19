'''
def register(phone,pwd):
	if phone.startswith("1") and len(phone) == 11:
		print("登陆成功")


def login(phone,pwd):
	if phone.startswith("1") and len(phone) == 11:
		print("登陆成功")

register("12345678909","123456")
login("12345678909","123456")
'''


def register(phone,pwd):
	result=isphone(phone)
	if result == True:
		print("登陆成功")
	else:
		print("登录失败")

def login(phone,pwd):
	result=isphone(phone)
	if result == True:
		print("登陆成功")
	else:
		print('登录失败')
def isphone(phone):
	if phone.startswith("1") and len(phone) == 11:
		return True
	else:
		return False

register("12345678909","123456")
login("12345678909","123456")
