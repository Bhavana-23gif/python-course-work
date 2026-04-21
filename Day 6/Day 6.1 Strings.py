Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> s = 'python programming lang'
>>> s.startswith('p')
True
>>> s.startswith('P')
False
>>> s.endswith('.ing')
False
>>> s.endswith('lang')
True
>>> s.isalpha()
False
>>> 'jnjhgygyikj'.isalpha()
True
>>> ' '.isalpha()
False
>>> 'python3.14'.isalpha()
False
>>> 'Pyathon'.isalpha()
True
>>> 'python'.isalnum()
True
>>> '123456'.isalnum()
True
>>> 'python123'.isalnum()
True
>>> 'python 123'.isalnum()
False
>>> 'python.123'.isalnum()
False
>>> 'p;.islower()
SyntaxError: unterminated string literal (detected at line 1)
>>> 'p'.islower()
True
>>> 'Python'.islower()
False
>>> 'PYthon'.isupper()
False
'PYTHON'.isupper()
True
'python 123'.islower()
True
'Python 123'.isupper()
False
'PYTHON 123'.isupper()
True
'     '.isspace()
True
'python 123'.isspace()
False
s
'python programming lang'
s.title()
'Python Programming Lang'
s.istitle()
False
'123myvar'.isidentifier()
False
'if'.isidentifier()
True
'12.3'.isdecimal()
False
'123'.isdecimal()
True
'12345'.isdigit()
True
'1/2'.isnumeric()
False
'११'.isnumeric()
True
'VIII'.isnumeric()
False
'VIII'.isnumeric()
False

