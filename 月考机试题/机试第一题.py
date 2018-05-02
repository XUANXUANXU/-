def check_score():
	list = []
	for i in range(5):
		list1 = []
		dict = {}
		while True:
			name = input("请输入学生姓名:")
			flag = 0
			for i in list:
				if name == i["name"]:
					flag = 1
					break
			if flag == 1:
				print("名字重复")
			yuwen = float(input("请输入语文成绩:"))
			shuxue = float(input("请输入数学成绩:"))
			tiyu = float(input("请输入体育成绩:"))
			list1.append(yuwen)
			list1.append(shuxue)
			list1.append(tiyu)
			

			dict["name"] = name
			dict["yuwen"] = yuwen
			dict["shuxue"] = shuxue
			dict["tiyu"] = tiyu

	

check_score()
