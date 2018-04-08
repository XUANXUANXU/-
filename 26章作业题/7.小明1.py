s = 7#距离
money = 0
a = 0
while a <= 60:

	if s <= 6:
		money = 3	
	elif 6 < s <= 12:
		money = 4
	elif 12 < s <= 22:
		money = 5
	elif 22 < s <= 32:
		money = 6
	elif s > 32:
		if s%32 == 0:
			money = 6+s/32
		else:
			money = 6 + int(s/32)+1
	if 100 <= money < 150:
		money = money*0.8
	if 	150 <= money < 400:
		money = money*0.5
		a+=1
print(money)
