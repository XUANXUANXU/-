print('名片系统'.center(30,"*"))
print('1:新增名片'.center(30," "))
print('2:查找名片'.center(30," "))
print('3:修改名片'.center(30," "))
print('4:删除名片'.center(30," "))
print('5:退出系统'.center(30," "))

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
		if flag == 1:
			print("名字重复了")
			continue
		job = input('请输入你的职位')
		phone = int(input('请输入你的联系电话'))
		company = input('请输入你的公司')
		address = input('请输入你的地址')

		card['name'] = name
		card['job'] = job
		card['phone'] = phone
		card['company'] = company
		card['address'] = address
		cards.append(card)
		print("新增成功")


	elif fun_number == 2:
		print('查找名片')
		name = input("请输入要查找的名字")
		flag = 0
		count = 0
		for i in cards:
			count+=1
			if name == i['name']:
				flag = 1
				break
		if flag == 1:
			print('姓名:%s\n职位:%s\n联系电话:%s\n公司:%s\n地址:%s\n'%(cards[count-1]['name'],cards[count-1]['job'],cards[count-1]['phone'],cards[count-1]['company'],cards[count-1]['address']))
		else:
			print('查无此人')

	elif fun_number == 3:
		name  = input("你输入要修改的名字")	
		for temp in cards:
			if name == temp["name"]:
				print("1:修改名字".center(30,"*"))
				print("2:修改职位".center(30,"*"))
				print("3:修改手机号".center(30,"*"))
				print("4:修改公司名称".center(30,"*"))
				print("5:修改公司地址".center(30,"*"))
				change_num = int(input("请选择修改序号"))
				if change_num == 1:
					name = input("请输入新的名字")
					temp["name"] = name
				elif change_num == 2:
					job = input("请输入新的职位")
					temp["job"] = job
				elif change_num == 3:
					phone = int(input("请输入手机号"))
					temp["phone"] = phone
				elif change_num == 4:
					company = input("请输入新的公司名")
					temp["company"] =company
				elif change_num == 5:
					address = input("请输入新的地址")
					temp["address"] = address
				else:
					print("输入有误\n")
	elif fun_number == 4:
		print('删除名片')
		name = input('请输入要删除的名字')
		flag = 0
		for i in cards:
			if name == i['name']:
				flag = 1
				sure_num = int(input('0请输入删除 1返回'))
				if sure_num == 0:
					cards.remove(i)
					print('删除成功')
				break
		if flag == 0:
			print("没有此人")
	else:
		print("退出系统")
		break
