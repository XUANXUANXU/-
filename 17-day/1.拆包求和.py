def sum(a,b,*args,**kwargs):
	all_sum = 0

	c =a+b
	all_sum+=c
	for i in args:
		all_sum+=i
	for i in kwargs.values():
		all_sum+=i
	print(all_sum)

k = (2,3,4,5,6,7)
d = {"age":189}
sum(1,2,*k,**d)
