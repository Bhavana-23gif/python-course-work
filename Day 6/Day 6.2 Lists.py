Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=[1,2,3,3]
l
[1, 2, 3, 3]
l=[]
type(l)
<class 'list'>
l=list()
l
[]
type(l)
<class 'list'>
l=[6,9.0,'dfghj',[],{},{1:1},True]
l
[6, 9.0, 'dfghj', [], {}, {1: 1}, True]
a=[1,2,3,4]
b=[7,8,9]
a+b
[1, 2, 3, 4, 7, 8, 9]
a*8
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
names = ['asif','sameer','mehaboob','priya','mahitha','bhavana']
names
['asif', 'sameer', 'mehaboob', 'priya', 'mahitha', 'bhavana']
names[0]
'asif'
names[-1]
'bhavana'
names[-4]
'mehaboob'
names[-3]
'priya'
names[-5]
'sameer'
names[4]
'mahitha'
names
['asif', 'sameer', 'mehaboob', 'priya', 'mahitha', 'bhavana']
names[1:3]
['sameer', 'mehaboob']
names[::2]
['asif', 'mehaboob', 'mahitha']
names[::-1]
['bhavana', 'mahitha', 'priya', 'mehaboob', 'sameer', 'asif']
names[-3:]
['priya', 'mahitha', 'bhavana']
names[:3]
['asif', 'sameer', 'mehaboob']
'asif' in names
True
'nagaraju' in names
False
'sai kiran' not in names
True
len(names)
6
sorted(names)
['asif', 'bhavana', 'mahitha', 'mehaboob', 'priya', 'sameer']
max(names)
'sameer'
min(names)
'asif'
names
['asif', 'sameer', 'mehaboob', 'priya', 'mahitha', 'bhavana']
id(names)
2635650763456
names[2]='mehaboob'
names
['asif', 'sameer', 'mehaboob', 'priya', 'mahitha', 'bhavana']
id(names)
2635650763456
names[0]='Asif'
names
['Asif', 'sameer', 'mehaboob', 'priya', 'mahitha', 'bhavana']
names[1]='Sameer'
names
['Asif', 'Sameer', 'mehaboob', 'priya', 'mahitha', 'bhavana']
id(names)
2635650763456
names.append('Abhi Ram')
names
['Asif', 'Sameer', 'mehaboob', 'priya', 'mahitha', 'bhavana', 'Abhi Ram']
names.insert(3,'Naga Raju')
names
['Asif', 'Sameer', 'mehaboob', 'Naga Raju', 'priya', 'mahitha', 'bhavana', 'Abhi Ram']
names.extend(['Yaswanth','dheshik','Sai Kiran'])
names
['Asif', 'Sameer', 'mehaboob', 'Naga Raju', 'priya', 'mahitha', 'bhavana', 'Abhi Ram', 'Yaswanth', 'dheshik', 'Sai Kiran']
names.insert(0,[12,'Naga Raju'])
names
[[12, 'Naga Raju'], 'Asif', 'Sameer', 'mehaboob', 'Naga Raju', 'priya', 'mahitha', 'bhavana', 'Abhi Ram', 'Yaswanth', 'dheshik', 'Sai Kiran']
names.pop(0)
[12, 'Naga Raju']
names
['Asif', 'Sameer', 'mehaboob', 'Naga Raju', 'priya', 'mahitha', 'bhavana', 'Abhi Ram', 'Yaswanth', 'dheshik', 'Sai Kiran']
'
names.pop(3)
'Naga Raju'
names
['Asif', 'Sameer', 'mehaboob', 'priya', 'mahitha', 'bhavana', 'Abhi Ram', 'Yaswanth', 'dheshik', 'Sai Kiran']
names.pop()
'Sai Kiran'
names.pop()
'dheshik'
names.pop()
'Yaswanth'
names
['Asif', 'Sameer', 'mehaboob', 'priya', 'mahitha', 'bhavana', 'Abhi Ram']
names.remove("Asif')
             
SyntaxError: unterminated string literal (detected at line 1)
names.remove('Asif')
             
names
             
['Sameer', 'mehaboob', 'priya', 'mahitha', 'bhavana', 'Abhi Ram']
names.remove('mehaboob')
             
names
             
['Sameer', 'priya', 'mahitha', 'bhavana', 'Abhi Ram']
del names[0]
             
names
             
['priya', 'mahitha', 'bhavana', 'Abhi Ram']
names.pop()
             
'Abhi Ram'
names
             
['priya', 'mahitha', 'bhavana']
names.clear()
             
names
             
[]
names=['Asif', 'Sameer', 'mehaboob', 'Naga Raju', 'priya', 'mahitha', 'bhavana', 'Abhi Ram', 'Yaswanth', 'dheshik', 'Sai Kiran']
             
names
             
['Asif', 'Sameer', 'mehaboob', 'Naga Raju', 'priya', 'mahitha', 'bhavana', 'Abhi Ram', 'Yaswanth', 'dheshik', 'Sai Kiran']
names.index('mehaboob')
             
2
names.index('dheshik')
             
9
names
             
['Asif', 'Sameer', 'mehaboob', 'Naga Raju', 'priya', 'mahitha', 'bhavana', 'Abhi Ram', 'Yaswanth', 'dheshik', 'Sai Kiran']
names.index('z')
             
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    names.index('z')
ValueError: list.index(x): x not in list
l=[1,1,1,1,12,3,4,5,6,6,7]
             
l.count(1)
             
4
l.count(6)
             
2
sorted(l)
             
[1, 1, 1, 1, 3, 4, 5, 6, 6, 7, 12]
s=set()
             
s
             
set()
l
             
[1, 1, 1, 1, 12, 3, 4, 5, 6, 6, 7]
l.sort()
             
l
             
[1, 1, 1, 1, 3, 4, 5, 6, 6, 7, 12]
l.sort(reverse=True)
             
l
             
[12, 7, 6, 6, 5, 4, 3, 1, 1, 1, 1]
l.reverse()
             
l
             
[1, 1, 1, 1, 3, 4, 5, 6, 6, 7, 12]
a=[1,2,3,4,5]
             
b=a
             
b
             
[1, 2, 3, 4, 5]
b.append(10)
             
a
             
[1, 2, 3, 4, 5, 10]
b
             
[1, 2, 3, 4, 5, 10]
b.append(13)
             
b
             
[1, 2, 3, 4, 5, 10, 13]
a
             
[1, 2, 3, 4, 5, 10, 13]
>>> c=a.copy()
...              
>>> id(a)
...              
2635606191936
>>> id(b)
...              
2635606191936
>>> id(c)
...              
2635650873024
>>> c.append(19)
...              
>>> c
...              
[1, 2, 3, 4, 5, 10, 13, 19]
>>> a
...              
[1, 2, 3, 4, 5, 10, 13]
>>> sum(a)
...              
38
>>> len(a)
...              
7
>>> any([0,0.0,'',[],{},set(),(),False])
...              
False
>>> any([1,0,0.0,'',[],{},set(),(),False])
...              
True
>>> all([1,0,0.0,'',[],{},set(),(),False])
...              
False
>>> all([1,2,3,5,True,12.4])
...              
True
