i = 1
a = 0#有a个整数能被5和7整除
while i <= 5000:
	if i%5 == 0 and i%7 == 0:
		print("%d能被5和7整除"%i)
		a+=1
	i+=1
print("一共有%d个"%a)
