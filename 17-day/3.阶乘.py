#5! = 5*4*3*2*1
#4! = 4*3*2*1
#5! = 5*4!
#4! = 4*3!
a = 1
b = 1
while a <= 5:
	b*=a
	a+=1
print(b)


def get_num(num):
	if num == 1:
		return 1
	else:
		return num*get_num(num-1)

a = get_num(5)
print(a)


'''
5*get_num(5-1)
4*get_num(4-1)
3*get_num(3-1)
2*get_num(2-1)
1
5*4*3*2*1
'''
