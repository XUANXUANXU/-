a = "123456"
p = "000000"
m = 1000

account = input("请输入账号:")
pwd = input("请输入密码:")

if account == a and pwd == p:
	print("可以取钱了")
	money = int(input("请输入取钱金额:"))
	if money<=m:
		print("取钱金额:%d\n剩余金额:%d"%(money,m-money))
	else:
		print("没钱取了")
else:
	print("非法账户")
