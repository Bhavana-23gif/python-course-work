Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s=set()
s={1,2,3,4,1,2,2,3,4,5}
s
{1, 2, 3, 4, 5}
s.add(100)
s
{1, 2, 3, 4, 5, 100}
s.add(10)
s
{1, 2, 3, 4, 5, 100, 10}
s.add(0)
s.add(30)
s
{0, 1, 2, 3, 4, 5, 10, 30, 100}
s
{0, 1, 2, 3, 4, 5, 10, 30, 100}
s.add(4.9)
s
{0, 1, 2, 3, 4, 5, 4.9, 10, 30, 100}
s.add('string')
s
{0, 1, 2, 3, 4, 5, 4.9, 10, 'string', 30, 100}
s.add((1,2,3))
s
{0, 1, 2, 3, 4, 5, 4.9, 10, 'string', 30, 100, (1, 2, 3)}
s
{0, 1, 2, 3, 4, 5, 4.9, 10, 'string', 30, 100, (1, 2, 3)}
a={1,2,3}
b={4,5}
a+b
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'set' and 'set'
a*3
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a*3
TypeError: unsupported operand type(s) for *: 'set' and 'int'
a[0]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a[0]
TypeError: 'set' object is not subscriptable
s[0:1]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s[0:1]
TypeError: 'set' object is not subscriptable
1 in s
True
2 not in s
False
for i in s:
    print(i)

0
1
2
3
4
5
4.9
10
string
30
100
(1, 2, 3)
a={9,8,7,1,2,3}
b={5,3,4,1,2,7}
a
{1, 2, 3, 7, 8, 9}
b
{1, 2, 3, 4, 5, 7}
a.union(b)
{1, 2, 3, 4, 5, 7, 8, 9}
a | b
{1, 2, 3, 4, 5, 7, 8, 9}
a
{1, 2, 3, 7, 8, 9}
b
{1, 2, 3, 4, 5, 7}
a.intersection(b)
{1, 2, 3, 7}
a&b
{1, 2, 3, 7}
a
{1, 2, 3, 7, 8, 9}
b
{1, 2, 3, 4, 5, 7}
a-b
{8, 9}
a^b
{4, 5, 8, 9}
a
{1, 2, 3, 7, 8, 9}
{1}<a
True
{9,10}<a
False
a>{1}
True
a>{1,2,3,4,5}
False
a>{1,2,8,9}
True
a
{1, 2, 3, 7, 8, 9}
b
{1, 2, 3, 4, 5, 7}
a.isdisjoint(b)
False
x={10,11}
a.isdisjoint(x)
True
a
{1, 2, 3, 7, 8, 9}
a.add(100)
a
{1, 2, 3, 100, 7, 8, 9}
a.add(50)
a
{1, 2, 3, 100, 50, 7, 8, 9}
a.update({70,80,90})
a
{1, 2, 3, 100, 70, 7, 8, 9, 80, 50, 90}
a.remove(100)
a
{1, 2, 3, 70, 7, 8, 9, 80, 50, 90}
a.remove(70)
a
{1, 2, 3, 7, 8, 9, 80, 50, 90}
a.pop()
1
a.pop()
2
a.pop()
3
a.clear()
a
set()
a={7, 8, 9, 80, 50, 90}
a.remove(7)
a
{80, 50, 8, 9, 90}
a.remove(7)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a.remove(7)
KeyError: 7
a.discard(7)
a
{80, 50, 8, 9, 90}
a
{80, 50, 8, 9, 90}
b
{1, 2, 3, 4, 5, 7}
a.add(7)
a
{80, 50, 7, 8, 9, 90}
b
{1, 2, 3, 4, 5, 7}
a.intersection(b)
{7}
a
{80, 50, 7, 8, 9, 90}
b
{1, 2, 3, 4, 5, 7}
a.intersection_update(b)
a
{7}
b
{1, 2, 3, 4, 5, 7}
>>> a
{7}
>>> b
{1, 2, 3, 4, 5, 7}
>>> b
{1, 2, 3, 4, 5, 7}
>>> c=b
>>> c.add(10)
>>> c
{1, 2, 3, 4, 5, 7, 10}
>>> b
{1, 2, 3, 4, 5, 7, 10}
>>> e=c.copy()
>>> e
{1, 2, 3, 4, 5, 7, 10}
>>> e.add(1000)
>>> e
{1, 2, 3, 4, 5, 7, 1000, 10}
>>> c
{1, 2, 3, 4, 5, 7, 10}
>>> len(c)
7
>>> max(c)
10
>>> min(c)
1
>>> sorted(c)
[1, 2, 3, 4, 5, 7, 10]
>>> sum(c)
32
>>> frozen = frozenset([1,2,3])
>>> frozen.add(4)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    frozen.add(4)
AttributeError: 'frozenset' object has no attribute 'add'
