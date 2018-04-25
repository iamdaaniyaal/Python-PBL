import enchant
import string
import random
d = enchant.Dict("en_US")
x = []
for i in range(10):
	a = random.choice(string.ascii_lowercase)
	x.append(a)
print(x)
for l in x:
	print(l)

flag=False
ip=input("Enter word")
c=len(ip)
for ch in ip:
	if(ch in x):
		flag = True
	else:
		flag  = False
		if(flag==False):
			break

# print(flag)


if(flag==True):
	if(d.check(ip)==True):
		print("your score is ",c)
	else:
		print("score=1")
		
if(flag==False):
	print("Error")
