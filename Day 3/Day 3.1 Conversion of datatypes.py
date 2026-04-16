Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
type(a)
<class 'int'>
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
bool(0)
False
b=10.3
int(b)
10
complex(b)
(10.3+0j)
str(b)
'10.3'
list(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
type(b)
<class 'float'>
c=10
c=10+3j
type(c)
<class 'complex'>
int(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(10+3j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
bool(c)
True
s="Python"
type(s)
<class 'str'>
int(s)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'Python'
float(s)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'Python'
complex(s)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
list(s)
['P', 'y', 't', 'h', 'o', 'n']
tuple(s)
('P', 'y', 't', 'h', 'o', 'n')
set(s)
{'y', 'o', 'h', 'n', 'P', 't'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(s)
True
l=[1, 2, 3, 4, 5]
type(l)
<class 'list'>
int(l)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    complex(l)
TypeError: complex() argument must be a string or a number, not list
str(l)
'[1, 2, 3, 4, 5]'
tuple(l)
(1, 2, 3, 4, 5)
set(l)
{1, 2, 3, 4, 5}
dict(l)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    dict(l)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
bool(l)
True
t=(1, 2, 3, 4, 5)
type(t)
<class 'tuple'>
int(t)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(t)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    complex(t)
TypeError: complex() argument must be a string or a number, not tuple
str(t)
'(1, 2, 3, 4, 5)'
list(t)
[1, 2, 3, 4, 5]
set(t)
{1, 2, 3, 4, 5}
dict(t)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    dict(t)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
bool(t)
True
e={1, 2, 3, 4, 5}
type(e)
<class 'set'>
int(e)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    int(e)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(e)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    float(e)
TypeError: float() argument must be a string or a real number, not 'set'
complex(e)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    complex(e)
TypeError: complex() argument must be a string or a number, not set
str(e)
'{1, 2, 3, 4, 5}'
list(e)
[1, 2, 3, 4, 5]
tuple(e)
(1, 2, 3, 4, 5)
dict(E)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    dict(E)
NameError: name 'E' is not defined. Did you mean: 'e'?
dict(e)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    dict(e)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
bool(e)
True
d={'name': 'bhavana', 'age': '21', 'course': 'python'}
type(d)
<class 'dict'>
int(d)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(d)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
complex(d)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    complex(d)
TypeError: complex() argument must be a string or a number, not dict
str(d)
"{'name': 'bhavana', 'age': '21', 'course': 'python'}"
list(d)
['name', 'age', 'course']
tuple(d)
('name', 'age', 'course')
set(d)
{'course', 'age', 'name'}
>>> bool(d)
True
>>> o='True'
>>> type(o)
<class 'str'>
>>> o=True
>>> type(o)
<class 'bool'>
>>> int(o)
1
>>> float(o)
1.0
>>> complex(o)
(1+0j)
>>> str(o)
'True'
>>> list(o)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    list(o)
TypeError: 'bool' object is not iterable
>>> tuple(o)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    tuple(o)
TypeError: 'bool' object is not iterable
>>> set(o)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    set(o)
TypeError: 'bool' object is not iterable
>>> dict(o)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    dict(o)
TypeError: 'bool' object is not iterable
