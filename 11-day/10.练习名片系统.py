print("名片系统".center(30,"*"))
print("1:增加名片".center(30," "))
print("2:查找名片".center(30," "))
print("3:修改名片".center(30," "))
print("4:删除名片".center(30," "))
print("5:退出系统".center(30," "))

list = []
while True:
	fun_number = int(input("请选择功能:"))
	if fun_number == 1:
		print("增加名片")
		flag = 0
		dict ={}
		name = input("请输入名字:")
		for temp in list:
			if name == temp['name']:
				flag = 1
				break
		if flag == 1:
			print("名字重复了")
			continue
		phone = int(input("请输入电话号码:"))
		job = input("请输入职位:")
		company = input("请输入公司名字:")
		address = input("请输入地址:")
		dict['name'] = name
		dict['phone'] = phone
		dict['job'] = job
		dict['company'] = company
		dict['address'] = address
		list.append(dict)
		print("新增成功\n")


	elif fun_number == 2:
		print("查找名片")
		find_name = input("请输入要查找的名字:")
		flag = 0
		count = 0
		for temp in list:
			count+=1
			if name == temp['name']:
				flag = 1
				break

		if flag == 0:
			print("查无此人\n")
		else:
			print("姓名:%s\n电话号码:%s\n职位:%s\n公司名字:%s\n地址:%s\n"%(list[count-1]['name'],list[count-1]['phone'],list[count-1]['job'],list[count-1]['company'],list[count-1]['address']))


	elif fun_number == 3:
		print("修改名片")
		change_name = input('请输入要修改的名字:')
		flag = 0
		for temp in list:
			if name == temp['name']:
				print("1:修改名字".center(30,"*"))
				print("2:修改电话号码".center(30,"*"))
				print("3:修改职位".center(30,"*"))
				print("4:修改公司名字".center(30,"*"))
				print("5:修改地址".center(30,"*"))
				change_number = int(input("请输入修改序号:"))
				if change_number == 1:
					name = input("请输入新的名字:")
					temp['name'] = name
				if change_number == 2:
					phone = int(input("请输入新的电话号码:"))
					temp['phone'] = phone
				if change_number == 3:
					job = input("请输入新的职位:")
					temp['job'] = job
				if change_number == 4:
					company = input("请输入新的公司名字:")
					temp['company'] = company
				if change_number == 5:
					address = input("请输入新的地址:")
					temp['address'] = address
				print("修改成功")
			else:
				print("输入有误:\n")
	elif fun_number == 4:
		print("删除名片")
		name = input ("请输入要删除的名字")
		flag = 0
		for temp in list:
			if name == temp['name']:
				flag = 1
				sure_num = int(input('确定要删除么1:确定 2:返回'))
				if sure_num == 1:
					list.remove(temp)
					print('删除成功')

				break
		if flag == 0:
			print("没有此人")


	

	elif fun_number == 5:
		print("退出系统")
		break

