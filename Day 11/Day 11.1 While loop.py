'''---------While loop-----------'''

''' 1 '''
i=20
while i>9:
    print(i)
    i=i-1

i=1
while i<11:
    print(i)
    i=i+1

i=1
while i<11:
    if i==5:
        break
    print(i)
    i=i+1

i=1
while i<11:
    i =i+1
    if i==5:
        continue
    print(i)

i=1
while i<11:
    if i==15:
        break
    print(i)
    i=i+1
else:
    print('1...10 numbers are printed')

l=[1,0,1,2,0,0,7,3,4,5,6,0,0,0,0,1,2,3,0,0,6,0,6,0,0,6]
while 0 in l:
    l.remove(0)
print(l)


assert print(b),'you forgot to define b'
assert a>10,'you forgot to define a'
