Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=20
b=10
a
20
b
10
a+b
30
a-b
10
a*b
200
a/b
2.0
a//b
2
10/3
3.3333333333333335
10//3
3
a%b
0
33%5
3
2**2
4
3**2
9
4**2
16
5**3
125
a**b
10240000000000
b**a
100000000000000000000
a
20
b
10
a>b
True
a>=b
True
a<b
False
a<=b
False
a==b
False
a!=b
True
c=10
c
10
c=c+10
c
20
c+=10
c
30
c-=20
c
10
c*=1000
c
10000
c//=20
c
500
c%=30
c
20
c**=2
c
400
c/=10
c
40.0
a
20
b
10
a%3==0
False
b%3==0
False
a%5==0 and b%5==0
True
a%5==0 and b205==0
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a%5==0 and b205==0
NameError: name 'b205' is not defined
a%20==0 and b%20==0
False
a%20==0 or b%20==0
True
not b%20==0
True
'python'
'python'
s='python'
'o' in s
True
'z' in s
False
'i' not in s
True
'o' not in s
False
l=['bhavana', 'mahitha', dhathri']
   
SyntaxError: unterminated string literal (detected at line 1)
l=['bhavana', 'mahitha', 'dhathri']
   
'bhavana' in l
   
True
'keerthy' in l
   
False
t=(1, 2, 3,4)
   
1 in t
   
True
5 in t
   
False
a=(1,2,3,4,5)
   
3 in a
   
True
7 in a
   
False
d={1:2,2:3,3:6,6:9}
   
9 in d
   
False
1 in d
   
True
l=[1,2,3,4]
   
l
   
[1, 2, 3, 4]
m=[1,2,3,4]
   
m
   
[1, 2, 3, 4]
n=m
   
n
   
[1, 2, 3, 4]
n==l
   
True
n==m
   
True
n is m
   
True
n is l
   
False
id(l)
   
2218982013696
>>> id(m)
...    
2218981903040
>>> id(n)
...    
2218981903040
>>> l is not n
...    
True
>>> m is not n
...    
False
>>> 12 & 13
...    
12
>>> 7 & 12
...    
4
>>> 7 | 12
...    
15
>>> 7^12
...    
11
>>> ~14
...    
-15
>>> ~13
...    
-14
>>> ~17
...    
-18
>>> 8<<2
...    
32
>>> 11>>1
...    
5
