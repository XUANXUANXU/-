list = []
name_list = []
count = 0
while True:
	if count == 3:
		break
	dict = {}
	
	#输入
	name = input('请输入你的名字')
	age = int(input('请输入你的年龄'))
	sex = input('请输入你的姓别')
	qq = int(input('请输入你的qq号'))
	weight = float(input('请输入你的体重'))

	#字典赋值
	if name not in name_list:
		dict['name'] = name
		dict['age'] = age
		dict['sex'] = sex
		dict['qq'] = qq
		dict['weight'] = weight

		#list = [{},{}]
		list.append(dict)
		name_list.append(dict['name'])

		print(list)
		count+=1
	else:
		print('名字重复')
age_sum = 0
#遍历
for i in list:
	age_sum+=i.get('age')
	print(i)
print("平均年龄是%.02d"%(age_sum/len(list)))
