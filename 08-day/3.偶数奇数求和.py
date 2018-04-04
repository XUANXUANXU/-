a = 1
b = 0#定义偶数和
c = 0#定义奇数和

while a <= 100:
	print(a)
	if a%2 == 0:#偶数
	   b+=a#和为偶数
	else:
	   c+=a#和为奇数

	a+=1
print("偶数是%d"%b)
print("奇数是%d"%c)
