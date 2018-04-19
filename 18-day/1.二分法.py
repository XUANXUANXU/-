list = [1,2,3,4,5,6,7,8,9,34,45,56,78]

key = 45
center = int(len(list)/2)

if key in list:
	while True:
		if list[center] > key:
			center = center-1
		elif list[center] < key:
			center = center+1
		elif list[center] == key:
			print("要找的数字是%d,索引是%d"%(key,center))
			break
else:
	print("没有该数字")

a = [1,2,3,4,5,6,7,8,9,12,23,34,45,56,67,78,89,90]
b = 78
c = int(len(a)/2)
if b in a:
	while True:
		if a[c] > b:
			c = c-1
		elif a[c] < b:
			c =c+1
		elif a[c] == b:
			print("要找的数字是%d,索引为%d"%(b,c))
			break
else:
	print("没有此数字")
