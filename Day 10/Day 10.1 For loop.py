''' for loop '''
'''sequence -  str,list,tuple,set,dict,range()'''

s='python'
for i in s:
    print(i)

l=[1,2,3,4]
for i in l:
    print(i)

t=(1,2,3,4,5)
for i in t:
    print(i)

s={1,2,3,4}
for i in s:
    print(i)

d={1:1,2:4,3:9,4:16,5:25}
for i in d:
    print(i,d[i])

for i in range(0,10,1):
    print(i)

for i in range(2,11,2):
    print(i)

for i in range(1,10,2):
    print(i)

for i in range(5,51,5):
    print(i)

for i in range(10,0,-1):
    print(i)

for i in range(20,9,-1):
    print(i)

for i in range(30,41):
    print(i)
    \

s='python'
for i in enumerate(s):
    print(i)

for i in range(len(s)):
    print(i)

for i in range(len(s)):
    print(i,s[i])

for i in enumerate(s):
    print(i[0],i[1])

names = ['abhiram','saikiran','yashwanth','dheshik']
for i in enumerate(names):
    print(i[0],i[1])

for i in range(len(names)):
    print(i,names[i])

s={1,2,3}
for i in enumerate(s):
    print(i[0],i[1])

d={1:1,2:4,3:9,4:16}
for i in enumerate(d):
    print(i)

for i in enumerate(d):
    print(i[0],i[1],d[i[1]])

'''break(terminate something in middle)  continue(it doesn't stop anywhere)  pass(to define a empty block of code)'''

for i in range(10):
    pass

for i in range(10):
    if i==5:
        break
    print(i)

for i in range(10):
    if i==5:
        continue
    print(i)


''' for with else  '''
products = ['bread','sugar','jam','butter']
a='sugar'
for i in products:
    if i==a:
        print(i)
        break
else:
    print("Not found")

pin=12345
for i in range(5):
    epin=int(input("Enter the pin: "))
    if pin==epin:
        print("Login successful")
        break
    else:
        print("Incorrect oin")
else:
    print("Try again after 60 seconds")


