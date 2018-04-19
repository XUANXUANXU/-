import time
def aclass():
	print('雪嫚正在上课玩手机')
	result = phone()
	if result == "兆刚住院了":
		print("雪嫚哭了")
	else:
		print("就那也吓得半死")

def phone():
	for i in range(15):
		print('手机刚好响了接电话去了')
		time.sleep(2)
	return "兆刚住院了"



aclass()
