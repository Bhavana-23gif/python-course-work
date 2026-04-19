Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> s='dfrf'
>>> s
'dfrf'
>>> type(s)
<class 'str'>
>>> s="dff"
>>> s='''fded'''
>>> s=''
>>> fname= 'abc'
>>> lname= 'xyz'
>>> fname + lname
'abcxyz'
>>> fname*7
'abcabcabcabcabcabcabc'
>>> fname*20
'abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc'
>>> '*'*30
'******************************'
>>> s='python'
>>> s[4]
'o'
>>> s[5]
'n'
>>> s[0]
'p'
>>> s[2]
't'
>>> s[3]
'h'
>>> s[-1]
'n'
>>> s[-2]
'o'
>>> s[-3]
'h'
>>> s[-4]
't'
names = 'bhavana mahitha priya keerthy asif'
names
'bhavana mahitha priya keerthy asif'
names[0]
'b'
names[-1]
'f'
names[-15]
'y'
names[-12]
'k'
names[9]
'a'
names[13]
'h'
names[0:7]
'bhavana'
names[8:15]
'mahitha'
names[16:21]
'priya'
names[22:30]
'keerthy '
names[31:]
'sif'
names[30:]
'asif'
names
'bhavana mahitha priya keerthy asif'
names[:15]
'bhavana mahitha'
names = 'bhavana mahitha asha krishna'
names
'bhavana mahitha asha krishna'
names[:15]
'bhavana mahitha'
names[-1:-7]
''
names[-1:-7:-1]
'anhsir'
names[-8:-1]
' krishn'
names[-13:-8]
' asha'
names[0:28:1]
'bhavana mahitha asha krishna'
names[0:28:2]
'baaamhtaah rsn'
names[::-1]
'anhsirk ahsa ahtiham anavahb'
names
'bhavana mahitha asha krishna'
'bhavana' in names
True
'asif' in names
False
'asha' in names
True
'bhavana' not in manes
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    'bhavana' not in manes
NameError: name 'manes' is not defined. Did you mean: 'names'?
'bhavana' not in names
False
names
'bhavana mahitha asha krishna'
len(names)
28
sorted(names)
[' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'h', 'h', 'h', 'h', 'h', 'i', 'i', 'k', 'm', 'n', 'n', 'r', 's', 's', 't', 'v']
max(names)
'v'
min(names)
' '
ord('a')
97
ord('A')
65
ord(' ')
32
ord('0')
48
chr(97)
'a'
chr(112)
'p'
chr(100)
'd'
chr(60)
'<'
chr(20)
'\x14'
chr(78)
'N'
names
'bhavana mahitha asha krishna'
names.upper()
'BHAVANA MAHITHA ASHA KRISHNA'
names.lower()
'bhavana mahitha asha krishna'
names.capitalize()
'Bhavana mahitha asha krishna'
names.title()
'Bhavana Mahitha Asha Krishna'
names
'bhavana mahitha asha krishna'
names='Bhavana Mahitha Asha Krishna'
names
'Bhavana Mahitha Asha Krishna'
names.swapcase()
'bHAVANA mAHITHA aSHA kRISHNA'
"AndréJoséEsmeré".casefold()
'andréjoséesmeré'
names.center(50,'*')
'***********Bhavana Mahitha Asha Krishna***********'
names.center(70,'-')
'---------------------Bhavana Mahitha Asha Krishna---------------------'
names.center(70,' ')
'                     Bhavana Mahitha Asha Krishna                     '
names.ljust(70,'-')
'Bhavana Mahitha Asha Krishna------------------------------------------'
names.rjust(70,'-')
'------------------------------------------Bhavana Mahitha Asha Krishna'
num='65789'
num.zfill(10)
'0000065789'
num.zfill(7)
'0065789'
num.zfill(5)
'65789'
num.zfill(15)
'000000000065789'
names
'Bhavana Mahitha Asha Krishna'
names.find('asha')
-1
names.find('Asha')
16
names.find('b')
-1
names.find('B')
0
names.find('n')
5
names.find('a')
2
names.rfind('a')
27
names.lfind('a')
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    names.lfind('a')
AttributeError: 'str' object has no attribute 'lfind'. Did you mean: 'find'?
names.index('a')
2
names.rindex('a')
27
names.index('z')
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    names.index('z')
ValueError: substring not found
names.count('a')
7
names.count('b')
0
names.count('c')
0
names.count('s')
2
names.count('h')
5
names.count('B')
1
names
'Bhavana Mahitha Asha Krishna'
names.replace('a','*')
'Bh*v*n* M*hith* Ash* Krishn*'
names.replace('i'.'0')
SyntaxError: invalid syntax
names.replace('i','0')
'Bhavana Mah0tha Asha Kr0shna'
names.replace('Asha','Hari')
'Bhavana Mahitha Hari Krishna'
names.replace('aeiou','*')
'Bhavana Mahitha Asha Krishna'
names.maketrans('aeiou','12345')
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
names.translate(names.maketrans('aeiou','12345'))
'Bh1v1n1 M1h3th1 Ash1 Kr3shn1'
names
'Bhavana Mahitha Asha Krishna'
names.split()
['Bhavana', 'Mahitha', 'Asha', 'Krishna']
names.rsplit(' ',2)
['Bhavana Mahitha', 'Asha', 'Krishna']
names.lsplit(' ',2)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    names.lsplit(' ',2)
AttributeError: 'str' object has no attribute 'lsplit'. Did you mean: 'rsplit'?
names.split(' ',2)
['Bhavana', 'Mahitha', 'Asha Krishna']
s='python\nprogramming\nlang'
s
'python\nprogramming\nlang'
s.splitlines()
['python', 'programming', 'lang']
l=['python', 'programming', 'lang']
','.join(1)
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    ','.join(1)
TypeError: can only join an iterable
','.join(l)
'python,programming,lang'
n=['Bhavana', 'Mahitha', 'Priya', 'Mehaboob', 'Asif']
','.join(n)
'Bhavana,Mahitha,Priya,Mehaboob,Asif'
'@'.join(n)
'Bhavana@Mahitha@Priya@Mehaboob@Asif'
names=['Bhavana', 'Mahitha', 'Priya', 'Mehaboob', 'Asif']
names
['Bhavana', 'Mahitha', 'Priya', 'Mehaboob', 'Asif']
names='Bhavana', 'Mahitha', 'Priya', 'Mehaboob', 'Asif'
names
('Bhavana', 'Mahitha', 'Priya', 'Mehaboob', 'Asif')
names.partition(' ')
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    names.partition(' ')
AttributeError: 'tuple' object has no attribute 'partition'
names
('Bhavana', 'Mahitha', 'Priya', 'Mehaboob', 'Asif')
names.partition(' ')
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    names.partition(' ')
AttributeError: 'tuple' object has no attribute 'partition'
names='Bhavana Mahitha Asha Krishna'
names
'Bhavana Mahitha Asha Krishna'
names.partition(' ')
('Bhavana', ' ', 'Mahitha Asha Krishna')
names.partition('A')
('Bhavana Mahitha ', 'A', 'sha Krishna')
names.partition('a')
('Bh', 'a', 'vana Mahitha Asha Krishna')
names.rpartition('a')
('Bhavana Mahitha Asha Krishn', 'a', '')
s='         hello       world'
s.strip()
'hello       world'
s.lstrip()
'hello       world'
s.rstrip()
'         hello       world'
s='     hello       world   '
s.rstrip()
'     hello       world'
s
'     hello       world   '
s.replace(' ','')
'helloworld'
text = 'Hello నమస్కారం नमस्ते @2026"
SyntaxError: unterminated string literal (detected at line 1)
text = 'Hello నమస్కారం नमस्ते @2026'
text.encode()
b'Hello \xe0\xb0\xa8\xe0\xb0\xae\xe0\xb0\xb8\xe0\xb1\x8d\xe0\xb0\x95\xe0\xb0\xbe\xe0\xb0\xb0\xe0\xb0\x82 \xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x87 @2026'
b'Hello \xe0\xb0\xa8\xe0\xb0\xae\xe0\xb0\xb8\xe0\xb1\x8d\xe0\xb0\x95\xe0\xb0\xbe\xe0\xb0\xb0\xe0\xb0\x82 \xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x87 @2026'.decode()
'Hello నమస్కారం नमस्ते @2026'
'😊'.encode()
b'\xf0\x9f\x98\x8a'
b'\xf0\x9f\x98\x8a'.decode()
'😊'
