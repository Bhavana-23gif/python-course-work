Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name = input()
bhavana
name
'bhavana'
type(name)
<class 'str'>
name = input("Enter the name: ")
Enter the name: bhavana
name
'bhavana'
age = input()
10
age
'10'
age = int(input("Enter the age: "))
Enter the age: 10
age
10
price = float(input("Enter the price: "))
Enter the price: 12.3
price
12.3
'1 2 3 4 5 6'.split()
['1', '2', '3', '4', '5', '6']
lang = input("Enter the lang: ").split()
Enter the lang: java html css dsa python
lang
['java', 'html', 'css', 'dsa', 'python']
names = input("Enter the names: ").split(',')
Enter the names: bhavana,mahitha,dhathri,keerthy,ramana
names
['bhavana', 'mahitha', 'dhathri', 'keerthy', 'ramana']
numbers = input("Enter the numbers: ").split()
Enter the numbers: 1 2 3 3
numbers
['1', '2', '3', '3']
int(['1', '2', '3', '3'])
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    int(['1', '2', '3', '3'])
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
map(int,['1', '2', '3', '4'])
<map object at 0x00000138C0AAFD00>
list(map(int,['1', '2', '3', '4']))
[1, 2, 3, 4]
numbers = list(map(int,input("Enter the nums: ").split()))
Enter the nums: 1 2 3 4 5 547
numbers
[1, 2, 3, 4, 5, 547]
numbers = list(map(float,input("Enter the nums: ").split()))
Enter the nums: 1.2 52.3 65.3 47.89
numbers
[1.2, 52.3, 65.3, 47.89]
numbers = list(map(str,input("Enter the names: ").split()))
Enter the names: bhavana mahitha priya keerthy
numbers
['bhavana', 'mahitha', 'priya', 'keerthy']
names = list(map(tuple,input("Enter the names: ").split()))
Enter the names: bhavana mahitha priya
names
[('b', 'h', 'a', 'v', 'a', 'n', 'a'), ('m', 'a', 'h', 'i', 't', 'h', 'a'), ('p', 'r', 'i', 'y', 'a')]
numbers = list(map(dict,input("Enter the names: ").split()))
Enter the names: name:bhavana age:21 course:python
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    numbers = list(map(dict,input("Enter the names: ").split()))
ValueError: dictionary update sequence element #0 has length 1; 2 is required
numbers = tuple(map(int,input("Enter the numbers: ").split()))
Enter the numbers: 1 2 3 4 5 6
numbers
(1, 2, 3, 4, 5, 6)
numbers = set(map(int,input("Enter the numbers: ").split()))
Enter the numbers: 1 5 6 8 9 
numbers
{1, 5, 6, 8, 9}
numbers = dict(map(int,input("Enter the numbers: ").split()))
Enter the numbers: name:bhavana course:python passed:2025
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    numbers = dict(map(int,input("Enter the numbers: ").split()))
ValueError: invalid literal for int() with base 10: 'name:bhavana'

names = dict(map(input("Enter the names: ").split()))
Enter the names: name:bhavana age:21 course:python
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    names = dict(map(input("Enter the names: ").split()))
TypeError: map() must have at least two arguments.
numbers = tuple(map(float,input("Enter the numbers: ").split()))
Enter the numbers: 1.2 3.5 6.89
numbers
(1.2, 3.5, 6.89)
names = tuple(input().split())
bhavana mahitha priya keerthy
names
('bhavana', 'mahitha', 'priya', 'keerthy')
names = set(input().split()))
SyntaxError: unmatched ')'

names = set(input().split())
bhavana mahitha priya keerthy
names
{'keerthy', 'bhavana', 'mahitha', 'priya'}
abcdefghijklmnopqrstuvwxyz
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    abcdefghijklmnopqrstuvwxyz
NameError: name 'abcdefghijklmnopqrstuvwxyz' is not defined

a,b,c=[1,2,3]
a
1
b
2
c
3
a,b,c=list(map(int,input().split()))
1 2 3
a
1
b
2
c
3
email,password = ['@gmail.com','pass@123']
email,password = input().split()
bhavana@gmail.com @2326
email,password
('bhavana@gmail.com', '@2326')
email
'bhavana@gmail.com'
password
'@2326'
a=eval(input())
12
a
12
a=eval(input())
12.6
a
12.6
a=eval(input())
'python'
a
'python'
a=eval(input())
['python', 'css', 'java']
a
['python', 'css', 'java']
a=eval(input())
('python', 'css', 'html', 'dsa')
a
('python', 'css', 'html', 'dsa')
a=eval(input())
{1,2,3,4,51}
a
{1, 2, 3, 4, 51}
a=eval(input())
[1 1 1]
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a=eval(input())
  File "<string>", line 1
    [1 1 1]
     ^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a=eval(input("Enter the input: "))
Enter the input: [1,1,1,2,3]
a
[1, 1, 1, 2, 3]
a=eval(input("Enter the input: "))
Enter the input: (1,2,3)
a
(1, 2, 3)
a=eval(input("Enter the input: "))
Enter the input: {1,2,3,4}
a
{1, 2, 3, 4}
a=eval(input("Enter the input: "))
Enter the input: {1:1,2:3,4:5,6:7}
a
{1: 1, 2: 3, 4: 5, 6: 7}
a=eval(input("Enter the input: "))
Enter the input: True
a
True
a,b,c=10,10.3,'python'
a
10
b
10.3
>>> c
'python'
>>> print(a,b,c)
10 10.3 python
>>> print("a=",a,'b=',b,'c=',c)
a= 10 b= 10.3 c= python
>>> print("a=",a,'b=',b,'c=',c,sep='')
a=10b=10.3c=python
>>> 
>>> print("a=",a,'b=',b,'c=',c,sep='\n')
a=
10
b=
10.3
c=
python
>>> print("a=",a,'b=',b,'c=',c,sep='@@@')
a=@@@10@@@b=@@@10.3@@@c=@@@python
>>> print("a=",a,'b=',b,'c=',c,sep='@@@',end='\n\n')
a=@@@10@@@b=@@@10.3@@@c=@@@python

>>> print("a=",a,'b=',b,'c=',c,sep='@@@',end='.....................')
a=@@@10@@@b=@@@10.3@@@c=@@@python.....................
>>> print(f'a={a}b={b}c={c}')
a=10b=10.3c=python
>>> print(f'a={a} b={b} c={c}')
a=10 b=10.3 c=python
>>> print('a=%d b=%f c=%s',%(a,b,c))
SyntaxError: invalid syntax
>>> print('a=%d b=%f.2f c=%s'%(a,b,c))
a=10 b=10.300000.2f c=python
>>> print('a={} b={} c={}'.format(b,c,a))
a=10.3 b=python c=10
>>> print('a=%d b=%.2f c=%s'%(a,b,c))
a=10 b=10.30 c=python
>>> print('a={} b={} c={}'.format(a,b,c))
a=10 b=10.3 c=python
>>> print('a={2} b={0} c={1}'.format(a,b,c))
a=python b=10 c=10.3
