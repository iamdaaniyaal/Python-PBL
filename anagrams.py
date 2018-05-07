import enchant
import string
import random

d = enchant.Dict("en_US")
x = []
'''
for i in range(10):
    a = random.choice(string.ascii_lowercase)
    x.append(a)
print(x)
for l in x:
    print(l)
'''
f=open("source.txt","r")
con=f.readlines()
'''
for i in con:
    for ch in i:
        print(ch)
        print("\n")
'''

for i in con:
    q=i
    for ch in range(len(q)):
        print(q[ch])
    flag = False
    ip = input("Enter word")
    c = len(ip)
    for ch in ip:
        if (ch in q):
            flag = True
            print(flag)
        else:
            flag = False
            print(flag)
            if flag == False:
                break

    # print(flag)

    if (flag == True):
        if (d.check(ip) == True):
            print("your score is ", c)
        else:
            print("score=1")

    if (flag == False):
        print("Error")




