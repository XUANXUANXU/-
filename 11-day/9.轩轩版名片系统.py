print('名片系统'.center(30,"*"))
print('1:新增名片'.center(30," "))
print('2:查找名片'.center(30," "))
print('3:修改名片'.center(30," "))
print('4:删除名片'.center(30," "))

cards = []
while True:
	fun_number = int(input('请选择功能'))
	if fun_number == 1:
		print('新增名片')
		flag = 0
		card = {}
		name = input('请输入你的名字')
		for i in cards:
			if name == i['name']:
				flag = 1
				break
		if flag = 1:
			print("名字重复了")
			continue
		job = input('请输入你的职位')
		phone = int(input('请输入你的联系电话'))
		company = input('请输入你的公司'))
		address = input('请输入你的地址')

		card['name'] = name
		card['job'] = job
		card['phone'] = phone
		card['company'] = company
		card['address'] = address
		cards.append(card)
		print("新增成功")

if fun_number == 2:
	print('查找名片')
if fun_number == 3:
	print('修改名片')
if fun_number == 4:
	print('删除名片')

