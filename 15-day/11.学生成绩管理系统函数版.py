print("学生成绩管理系统".center(30,"*"))
print("")
list = []
number = int(input("请选择功能序号"))
while True:
	if number == 0:
		print("打印菜单".center(30,"*"))
		print("1:录入成绩\n2:查询成绩\n3:修改成绩\n4:删除成绩\n5:打印全部成绩\n6:退出系统")
		num = int(input("请继续选择功能序号"))
		if num == 1:
			print("录入成绩")
			flag = 0
			dict = {}
			xuehao = int(input("请输入学号"))
			for i in list:
				if xuehao == i["xuehao"]:
					flag = 1
					break
				if flag == 1:
					print("学号重复无法添加")
					continue
			name = input("请输入名字")
			kemu = input("请输入科目")
			fenshu = float(input("请输入分数"))
			dict["xuehao"] = xuehao
			dict["name"] = name
			dict["kemu"] = kemu
			dict["fenshu"] = fenshu
			list.append(dict)
			print("录入成功\n")
		elif num == 2:
			print("查询成绩")
			find_xuehao = int(input("请输入要查找的学号"))
			flag = 0
			count = 0
			for i in list:
				count += 1
				if xuehao == i['xuehao']:
					flag = 1
					break
			if flag == 1:
				print("学号%s\n名字%s\n科目%s\n分数%s\n"%(list[count-1]['xuehao'],list[count-1]['name'],list[count-1]['kemu'],list[count-1]['fenshu']))
			else:
				print("查无此人")
		elif num == 3:
			print("修改成绩")
			change_xuehao = int(input("请输入要修改的学号"))
			flag = 0
			for i in list:
				if xuehao == i["xuehao"]:
					print("1:修改学号".center(30,"*"))
					print("2:修改名字".center(30,"*"))
					print("3:修改科目".center(30,"*"))
					print("4:修改分数".center(30,"*"))
					change_num = int(input("请选择修改序号"))
					if change_num == 1:
						xuehao = input("请输入新的学号")
						i["xuehao"] = xuehao
					elif change_num == 2:
						name = input("请输入新的名字")
						i["name"] = name
					elif change_num == 3:
						kemu = int(input("请输入科目"))
						i["kemu"] = kemu
					elif change_num == 4:
						fenshu = input("请输入新的分数")
						i["fenshu"] =fenshu
					else:
						print("输入有误\n")
		 elif num == 4:
			print("删除成绩")
			xuehao = int(input("请输入要删除的学号"))
			flag = 0
			for i in list:
				if xuehao = i['xuehao']:
					flag = 1
			
		elif num == 5:
			print("打印全部成绩")
		elif num == 6:
			print("退出系统")
			break
