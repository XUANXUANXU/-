def hehe():
	list = [{"beijing":{"mianji":129,"renkou":123},"shanghai":{"mianji":888,"renkou":666}}]
	for i in list:
		for j in i:
			for x in i[j]:
				print(j,x,i[j][x])

hehe()
