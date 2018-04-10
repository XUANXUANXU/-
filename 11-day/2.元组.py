t = ('幼儿园','小学','中学','大学')
i = input('请输入一个名字')

if i in list(t):
	print("你眼光真差")
else:
	print("还不错欧")


if i not in t:
	print("还不错欧")
else:
	print("你眼光真差")
