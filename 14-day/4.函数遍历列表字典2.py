def haha():
	list = [{"beijing":{"mianji":129,"renkou":123},"shanghai":{"mianji":888,"renkou":666}}]
	for i in list:
		for k,v in i.items():
			for j,l in v.items():
				print(k,j,l)
haha()
