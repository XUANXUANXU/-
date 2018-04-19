def shoujihao(phone):
	phone = input("请输入手机号")
	if phone.startswith("1") and len(phone) == 11:
		return True
	else:
		return False

phone = input("请输入手机号")
result = shoujihao(phone)
if result == False:
	print("输入错误")


phone2 = input("请输入手机号")
result = shoujihao(phone2)
if result == False:
	print("手机号错误")
