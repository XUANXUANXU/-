cards = []
while True:
	flag = 0
	card = {}
	name = input("请输入名字")
	for i in cards:
		if name == i['name']:
			flag = 1
			break
	if flag == 1:
		print('名字重复')
		continue
	age = int(input("请输入年龄"))
	company = input("请输入公司")
	address = input("请输入地址")
	job = input("请输入职位")

	card['name'] = name
	card['age'] = age
	card['company'] = company
	card['address'] = address
	card['job'] = job
	cards.append(card)
	print('新增成功')
