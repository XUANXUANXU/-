st= [["传奇","贪玩蓝月"],["QQ飞车","QQ炫舞"],["天天酷跑","天天炫斗"],["王者荣耀","绝地求生"]]
for i in st:
	for j in i:
		print('这个游戏叫%s'%j)



i = 0
while i < len(st):
	#print(st[i])
	j = 0
	while j < len(st[i]):
		print(st[i][j])
		j+=1
	i+=1
