names = ['妲己','虞姬','不知火舞','貂蝉','安琪拉','蔡文姬']
for i in names:
	print("*"+i)

print("*"*50)

cars = ['喜羊羊','美羊羊','懒洋洋','沸羊羊','慢羊羊']
for i in cars:
	print("我喜欢骑%s"%i)

print("*"*50)

names1 = ['秦始皇','雍正','康熙','刘邦']#原名单
for i in names1:
	print("%s和我一起用餐"%i)
print("邀请了%s个嘉宾共进晚餐"%len(names1))
print("%s因病无法赴约"%names1[0])
names1[0] = "黑寡妇"
for i in names1:
	print("%s和我一起用餐"%i)
print("邀请了%s个嘉宾共进晚餐"%len(names1))
print("因为有了一个更大的包间")
names1.insert(0,'张飞')
names1.insert(3,'刘备')
names1.append('曹操')
for i in names1:
	print("%s和我一起用餐"%i)
print("邀请了%s个嘉宾共进晚餐"%len(names1))
print("因为餐桌不够只能邀请两位嘉宾了")
for i in range (len(names1)):
	if len(names1) == 2:
		break
	print("%s你别来了不好意思桌子不够大"%names1[0:1])
	names1.pop(0)
for i in names1:
	print("%s你依然在受邀行列"%i)
print("邀请了%s个嘉宾共进晚餐"%len(names1))
del names1[0:2]
print(names1)
