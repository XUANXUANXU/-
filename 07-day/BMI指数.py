#小明的BMI指数
height = float(input("请输入身高"))
weight = float(input("请输入体重"))
BMI指数 = weight/(height**2)


if BMI指数 < 18.5:
	print("过轻")
elif 18.5 < BMI指数 < 25:
	print("正常")
elif 25 < BMI指数 < 28:
	print("过重")
elif 28 < BMI指数 < 32:
	print("肥胖")
else:
	print("严重肥胖")

print(BMI指数)

