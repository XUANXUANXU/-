cards = []
def mingpian():
	print("名片管理系统".center(30," "))
	print("1:增加名片".center(30," "))
	print("2:查找名片".center(30," "))
	print("3:修改名片".center(30," "))
	print("4:删除名片".center(30," "))
	print("5:打印名片".center(30," "))
def input_fun():
	while True:
		input_fun = int(input("请选择功能"))
		if input_fun == 1:
			add_card()
		elif input_fun == 2:
			find_card()
		elif input_fun == 3:
			change_card()
		elif input_fun == 4:
			del_card()
		elif input_fun == 5:
			all_card()
		else:
			break
def add_card():
		print("增加名片")
		card = {}
		flag = 0
		name = input("请输入名字")	
		for temp in cards:
			if name == temp['name']:
				flag = 1
				break
		if flag == 1:
			print("名字重复了")
			return
		job = input("请输入职位")
		company = input("请输入公司")
		phone = int(input("请输入手机号"))
		card["name"] = name
		card["job"] = job
		card["company"] = company
		card["phone"] = phone
		cards.append(card)
		print("新增成功")
def find_card():
	print("查找名片")
	name = input("请输入要查找的名字")
	flag = 0
	for temp in cards:
		if name == temp['name']:
			print("名字:%s\n职位:%s\n公司:%s\n手机号:%d\n"%(temp['name'],temp['job'],temp['company'],temp['phone']))
			flag = 1
	if flag == 0:
		print('查无此人')
def change_card():
	print("修改名片")
	name = input("请输入要修改的名字")
	for temp in cards:
		if name == temp['name']:
			print("1:修改名字")
			print("2:修改职位")
			print("3:修改公司")
			print("4:修改手机号")
			change_num = int(input("请输入要修改的序号"))
			if change_num == 1:
				new_name = input("请输入新的名字")
				temp['name'] = new_name
			elif change_num == 2:
				new_job = input("请输入新的职位")
				temp['job'] = new_job
			elif change_num == 3:
				new_company = input("请输入新的公司")
				temp['company'] = new_company
			elif change_num == 4:
				new_phone = input("请输入新的电话")
				temp['phone'] = new_phone
			else:
				print("输入有误")

			
def del_card():
	print("删除名片")
	name = input("请输入要删除的名字")
	for temp in cards:
		if name == temp['name']:
			cards.remove(temp)
			print("删除成功")
		else:
			print("无法删除")
			
def all_card():
	print("打印名片")
	print("名字".center(8," "),end="")
	print("职位".center(8," "),end="")
	print("公司".center(8," "),end="")
	print("手机号".center(8," "))
	for temp in cards:
		
		print("%s\t%s\t%s\t%d\t"%(temp['name'],temp['job'],temp['company'],temp['phone']))
mingpian()
input_fun()
