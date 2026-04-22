Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d={}
d=dict()
type(d)
<class 'dict'>
d={'name':='asif','batch':52,'skills':['python','css','html']}
SyntaxError: cannot use assignment expressions with literal
d={'name':'asif','batch':52,'skills':['python','css','html']}
d['name']='mehaboob'
d
{'name': 'mehaboob', 'batch': 52, 'skills': ['python', 'css', 'html']}
d
{'name': 'mehaboob', 'batch': 52, 'skills': ['python', 'css', 'html']}
d['course']='mehaboob'
d
{'name': 'mehaboob', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'mehaboob'}
s={}
s[1]='int'
s
{1: 'int'}
s[1.2]='float'
s['demo']='string'
s
{1: 'int', 1.2: 'float', 'demo': 'string'}
s[(1,2,3)]='tuple'
s
{1: 'int', 1.2: 'float', 'demo': 'string', (1, 2, 3): 'tuple'}
s[False]=1
s
{1: 'int', 1.2: 'float', 'demo': 'string', (1, 2, 3): 'tuple', False: 1}
s
{1: 'int', 1.2: 'float', 'demo': 'string', (1, 2, 3): 'tuple', False: 1}
a={1:1}
b={2:2}


s
{1: 'int', 1.2: 'float', 'demo': 'string', (1, 2, 3): 'tuple', False: 1}
d
{'name': 'mehaboob', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'mehaboob'}
'name' in d
True
'mehaboob' in d
False
d
{'name': 'mehaboob', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'mehaboob'}
d['name']
'mehaboob'
d['skills']
['python', 'css', 'html']
d['course']
'mehaboob'
d.get('age')
d.get('course')
'mehaboob'
d.get('age','age is not present')
'age is not present'
d.get('name','name is not present')
'mehaboob'

d
{'name': 'mehaboob', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'mehaboob'}
d['course':'PFS']
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    d['course':'PFS']
KeyError: slice('course', 'PFS', None)
d['course']='PFS'
d
{'name': 'mehaboob', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS'}
d['age']=21
d
{'name': 'mehaboob', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 21}
d.update({'k1':'v1'.'k2':'v2'})
SyntaxError: invalid syntax
d.update({'k1':'v1','k2':'v2'})
d
{'name': 'mehaboob', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 21, 'k1': 'v1', 'k2': 'v2'}
d.popitem()
('k2', 'v2')
d.popitem()
('k1', 'v1')
d
{'name': 'mehaboob', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 21}
d.pop('name')
'mehaboob'
d
{'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 21}
d
{'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 21}
del d['batch']
d
{'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 21}
>>> d.clear()
>>> d
{}
>>> d={'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 21}
>>> d
{'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 21}
>>> d.keys()
dict_keys(['batch', 'skills', 'course', 'age'])
>>> d.values()
dict_values([52, ['python', 'css', 'html'], 'PFS', 21])
>>> d.items()
dict_items([('batch', 52), ('skills', ['python', 'css', 'html']), ('course', 'PFS'), ('age', 21)])
>>> sorted(d)
['age', 'batch', 'course', 'skills']
>>> len(d)
4
>>> max(d)
'skills'
>>> min(d)
'age'
>>> '
SyntaxError: unterminated string literal (detected at line 1)
>>> 
>>> d
{'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 21}
>>> d.get('name')
>>> d.setdefault('name','')
''
>>> d
{'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 21, 'name': ''}
>>> d.get('age')
21
>>> d.setdefault('age',24)
21
>>> d
{'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'PFS', 'age': 21, 'name': ''}
