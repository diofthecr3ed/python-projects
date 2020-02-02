
#def newfunction(your_text):
#	b =  your_text[3:6] +your_text[0:3]+ your_text[9:12] + your_text[6:9] + your_text[15:18] + your_text[12:15] + your_text[24:28] + your_text[18:24]
#	return b

#x = newfunction("this is example text ")
#print(x)
#
#def newfunction_(your_text_):
#	b =  your_text_[3:6] +your_text_[0:3]+ your_text_[9:12] + your_text_[6:9] + your_text_[15:18] + your_text_[12:15] + your_text_[24:28] + your_text_[18:24]
#	return b
#y = newfunction_("s ithixams e teplext ")
#rint(y)

#print(ord(" "))
#print(chr(34))


#def newfunction(your_text):
#	b = list(your_text)
#	return b
#
#x = newfunction("hello world")
#result=[]
#for a in list(x):
#	result.append(chr(ord(a)+2))
#
#
#
#
#
#s2=""
#s2=s2.join(result)
#print(s2)
#
#
#def newfunction_(your_text_):
#	c = list(your_text_)
#	return c
#
##decryption
#result_=[]
#for b in list(result):
#	result_.append(chr(ord(b)-2))
#
#
#
#s1=""
#s1=s1.join(result_)
#print(s1)

#a=[1,2,3,4,5]
#for i in range(len(a)):
#	x=a.pop()
#	a.insert(i,x)
#	print(a)
	

s1 = "abbcc"
s2 = "cabbc"

for i in range(len(s1)):

	s1=s1[1:]+s1[0]
	print(s1)
	if(s1==s2):
		print("yes, it is a rotated version")


