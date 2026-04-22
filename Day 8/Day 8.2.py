Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
my_set = {1, 2, 3, 4}
my_set
{1, 2, 3, 4}
empty_set = set()
empty_set
set()
set_with_duplicates = {1, 2, 2, 3, 4}
>>> print(set_with_duplicates)
{1, 2, 3, 4}
>>> invalid_set = {[1, 2], 3}
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    invalid_set = {[1, 2], 3}
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
>>> my_set = {1, 2, 3, 4}
>>> print(3 in my_set)
True
>>> print(5 not in my_set)
True
>>> set1 = {1, 2, 3}
>>> set2 = {3, 4, 5}
>>> result = set1 | set2
>>> result
{1, 2, 3, 4, 5}
>>> set1 = {1, 2, 3}
>>> set2 = {3, 4, 5}
>>> result = set1 & set2
>>> result
{3}
>>> result = set1 - set2
>>> result
{1, 2}
>>> result = set1 ^ set2
>>> result
{1, 2, 4, 5}
>>> print(set1 <= set2)
False
>>> print(set1 >= set2)
False
>>> print(set1.isdisjoint(set2))
False
>>> frozen = frozenset([1, 2, 3])
>>> print(frozen)
frozenset({1, 2, 3})
