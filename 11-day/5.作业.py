a = []
b = 0
c = []
while b < 3:
	d = {}
	x = {}
	x['名字'] = input('请输入名字')
	if x in c:
		print('姓名重复请重新输入')
		continue
	c.append(x)
	d['年龄'] = int(input("请输入年龄"))
	d['性别'] = input('请输入性别')
	d['qq'] = int(input("请输入qq"))
	d['体重'] = float(input("请输入体重"))
	d.update(x)
	a.append(d)
	b+=1
for i in a:
	for k,v in i.items():
		print("%s的值是%s"%(k,v))
z = 0
for i in a:
	z+=i['年龄']
print("平均年龄为%.02f"%(z/len(a)))
