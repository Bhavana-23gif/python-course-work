Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t=()
t=tuple()
type(t)
<class 'tuple'>
t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t=(1,2.3,'string',[1,2,3],{1,2,3},(1,2,3),{1:1,2:2},False)
t
(1, 2.3, 'string', [1, 2, 3], {1, 2, 3}, (1, 2, 3), {1: 1, 2: 2}, False)
l=(1,1,1,1,1)
l
(1, 1, 1, 1, 1)
a=(1,2,3)
b=(4,5,6)
a+b
(1, 2, 3, 4, 5, 6)
a*3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
a
(1, 2, 3)
a[2]
3
t
(1, 2.3, 'string', [1, 2, 3], {1, 2, 3}, (1, 2, 3), {1: 1, 2: 2}, False)
t[1:4]
(2.3, 'string', [1, 2, 3])
t[-3:]
((1, 2, 3), {1: 1, 2: 2}, False)
t[2]
'string'
t[-1]
False
'string' in t
True
(1,2,3) in t
True
(7,8) in t
False
'nhgik' in t
False
len(t)
8
t=(1,2,3,4,5,6,7,8,9)
max(t)
9
min(t)
1
sorted(t)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
t.count(1)
1
a,b=(1,2)
a
1
b
2
>>> a=(1,2,3,4)
>>> w,x,y,z=a
>>> w
1
>>> x
2
>>> y
3
>>> z
4
>>> a
(1, 2, 3, 4)
>>> a.index(4)
3
>>> sum(a)
10
>>> a
(1, 2, 3, 4)
>>> t
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> t=(1,2,3,[4,5])
>>> t
(1, 2, 3, [4, 5])
>>> t.append(10)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    t.append(10)
AttributeError: 'tuple' object has no attribute 'append'
>>> t[3]
[4, 5]
>>> t[3].append(10)
>>> t
(1, 2, 3, [4, 5, 10])
>>> t[3].pop()
10
>>> t
(1, 2, 3, [4, 5])
