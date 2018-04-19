fun = lambda a,b:a+b
print(fun(3,4))

fun = lambda a,b=3:a+b
print(fun(3))


def haha(a,b,fun):
	result  = fun(a,b)
	print(result)
	print(fun(a,b))
haha(4,5,lambda x,y:x+y)




