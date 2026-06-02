Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='python programming'
len(s)
18
sorted(s)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
min(s)
' '
max(s)
'y'
ord('A')
65
ord('a')
97
ord('o')
111
ord('0')
48
ord('')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    ord('')
TypeError: ord() expected a character, but string of length 0 found
ord(' ')
32
chr(98)
'b'
chr(120)
'x'
chr(30)
'\x1e'
chr(35)
'#'
chr(37)
'%'
chr(32)
' '
chr(65)
'A'
s='python Programming'

s.upper()
'PYTHON PROGRAMMING'
s.lower
<built-in method lower of str object at 0x0000016A6CC98770>
s.lower()
'python programming'
s.capitalize()
'Python programming'
s.title()
'Python Programming'
s.swapcase()
'PYTHON pROGRAMMING'
"STRAẞEMÁLAGAÅngströmCafé".casefold()
'strassemálagaångströmcafé'
s
'python Programming'
s.center(38,'*')
'**********python Programming**********'
s.center(28'-')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> s.center(28,'-')
'-----python Programming-----'
>>> s.ljust(28,'-')
'python Programming----------'
>>> s.rjust(28,'-')
'----------python Programming'
>>> '123'.zfill(5)
'00123'
>>> '123'.zfill(10)
'0000000123'
>>> '123'.zfill(3)
'123'
>>> '123'.zfill(2)
'123'
>>> s
'python Programming'
>>> s.find('o')
4
>>> s.find('g')
10
>>> s.rfind('o')
9
>>> s.find('z')
-1
>>> s.index('o')
4
>>> s.rindex('o')
9
>>> s.index('z')
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    s.index('z')
ValueError: substring not found
>>> s
'python Programming'
>>> s.count('y')
1
>>> s.coumt('m')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    s.coumt('m')
AttributeError: 'str' object has no attribute 'coumt'. Did you mean: 'count'?
>>> s.count('m')
2
>>> s.count('g')
2
