num1=input('Enter your first number -->')
num2=input('Enter your second number -->')

def add(x,y):
	return(x+y)
def sub(a,b):
	return(a-b)
def mul(r,s):
	return(r*s)
def div(c,d):
	return(c/d)

op=input('Operator')
if (op=='+'):
	c=add(num1,num2)
	print(c)
elif(op=='-'):
	c=sub(num1,num2)
	print(c)
elif(op=='*'):
	c=mul(num1,num2)
	print(c)
elif(op=='/'):
	c=div(num1,num2)
	print(c)

