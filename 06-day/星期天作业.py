#个人名片
name = input("请输入姓名:")
company = input("请输入公司:")
title = input("请输入职位:")
phone = input("请输入电话:")
email = input("请输入邮箱:")

print("*"*50)

print(name)
print(company)
print(title)
print(phone)
print(email)

print("*"*50)
print("姓名:%s"% name)
print("公司:%s"% company)
print("职位:%s"% title)
print("电话:%s"% phone)
print("邮箱:%s"% email)

print("*"*50)
#print("姓名%s\n"%name,"公司%s\n"%company,"职位%s\n"%title,"电话%s\n"%phone,"邮箱%s\n"%email) 
print("姓名:%s\n公司:%s\n职位:%s\n电话:%s\n邮箱:%s\n"%(name,company,title,phone,email))

print("*"*50)
#ATM取款机系统
account = input("请输入你的账号")
password = input("请输入你的密码")
nick_name = input("请输入姓名")
money = 1999#原有的金额
need_money = input("请输入需要的金额")
sum = money - int(need_money)
print("账号:%s\n密码:******\n姓名:%s原来的金额:%d\n需要的金额%s\n剩下的金额%d"%(account,nick_name,money,need_money,sum))

#入职手续
print("*"*50)

name = input("请输入你的名字")
age = int(input("请输入你的年龄"))
sex = input("请输入你的性别")
high = float(input("请输入身高"))
weight = float(input("请输入体重"))
ID_number = int(input("请输入身份证号"))
birthday = input("请输入生日")
phone = int(input("请输入电话号码"))
print("*"*50)
print("名字:%s\n"%(name))
print("*"*50)

#便利店收银系统
name = input("请输入商品名字")
price = float(input("请输入商品价格"))
weight = float(input("请输入商品重量"))
print("*"*50)
print("商品名字:%s"%(name))
print("商品名字:%s\n商品价格:%s\n商品重量:%s"%(name,price,weight))

#房屋销售系统
print("*"*50)
size = input("请输入房屋大小")
area = float(input("请输入房屋面积"))
city = input("请输入所在城市")
plase = input("请输入位置")
price = float(input("请输入价格"))
counselor = input("请输入顾问")
print("*"*50)
print("房屋大小:%s\n房屋面积:%s\n城市:%s\n位置:%s\n价格:%s\n顾问:%s"%(size,area,city,plase,price,counselor))


#作业

print("*"*50)
print("一年=%s秒"%(60*60*24*365))
print("一公里=%s毫米"%(1000*1000))

print("*"*50)
x = 2
print(x**2)
print(6*(x/7))
print(6/(4+5*x))


