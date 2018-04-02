#判断年龄是否正确

age = int(input("请输入年龄"))
if 0<=age<=120:
	print("正确")

else:
	print("错啦")

#王者荣耀
hero = str(input("请输入名称"))
if hero == "ADC":
	print("黄忠 虞姬 后裔")

elif hero == "法师":
	print("王昭君 妲己 安琪拉")

elif hero == "肉":
	print("亚瑟 程咬金")

elif hero == "刺客":
	print("阿珂 李白 兰陵王")
