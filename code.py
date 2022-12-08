
def simple(r,t,p):
	result=1 + (r*t)
	result2=result * p
	print("simple interest is :")
	print(result2)

def compound(r,n,t,p):
	result3=1+(r/n)
	result4=result3 * (n*t)
	result5=result4 * p
	print("compound interest is:")
	print(result5)

simple(2.5,3,2000)
compound(2.5,2,3,2000)


