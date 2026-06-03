Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='    hello    world     '
s
'    hello    world     '
s.strip()
'hello    world'
s.lstrip()
'hello    world     '
s.rstrip()
'    hello    world'
s='strings.py'
s
'strings.py'
s.startswith('srt')
False
s.startwith('str')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s.startwith('str')
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
s.startswith('str')
True
s.startswith('ghf')
False
s.endswith('py')
True
s.endswith('js')
False
'sdfyui'.isalpha()
True
'DSFGHJKLTrryghjutyghj'.isalpha()
True
'RAM@123456789'.isalpha()
False
'edfggdgyg'.islower()
True
'dasffhdffkhdm12345@#$%%'.islower()
True
'ABCDEFGHIJKA$%#@&^*^'isupper()
SyntaxError: invalid syntax
'ABCDEFGHIJKA$%#@&^*^'.isupper()
True
' '.isspace()
True
'hello      '.isspace()
False
'Py Python'.istittle()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    'Py Python'.istittle()
AttributeError: 'str' object has no attribute 'istittle'. Did you mean: 'istitle'?
'Py Python'.istitle()
True
'Py python'.istitle()
False
'py_python'.isidentifier()
True
'py@123'.isidentifier()
False
l=[]
l=list()
type(l)
<class 'list'>
l=[1,2,3,4]
m=[5,6,7,8]
l+m
[1, 2, 3, 4, 5, 6, 7, 8]
l*4
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
l[10,20,30,40,50]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    l[10,20,30,40,50]
TypeError: list indices must be integers or slices, not tuple
l=[10,20,30,40,50]
l[4]
50
l[3]
40
l[1]
20
l[-4]
20
l[-3]
30
l[-5]
10
l
[10, 20, 30, 40, 50]
l[:3]
[10, 20, 30]
l[3:]
[40, 50]
l[1:4]
[20, 30, 40]
l[::-1]
[50, 40, 30, 20, 10]
l[-1:-4:-1]
[50, 40, 30]
l[-3::-1]
[30, 20, 10]
l
[10, 20, 30, 40, 50]
20 ib l
SyntaxError: invalid syntax
20 in l
True
40 in l
True
70 not in l
True
10 in l
True
80 in l
False
l
[10, 20, 30, 40, 50]
id(l)
2931419827136
l[1]
20
l[1]=70
l
[10, 70, 30, 40, 50]
id(l)
2931419827136
l[4]=100
l
[10, 70, 30, 40, 100]
l.append(120)
l
[10, 70, 30, 40, 100, 120]
l.append(400)
l
[10, 70, 30, 40, 100, 120, 400]
l.insert(1,60)
l
[10, 60, 70, 30, 40, 100, 120, 400]
l.insert(4,50)
l
[10, 60, 70, 30, 50, 40, 100, 120, 400]
l.extend([80,90,110])
l
[10, 60, 70, 30, 50, 40, 100, 120, 400, 80, 90, 110]
l
[10, 60, 70, 30, 50, 40, 100, 120, 400, 80, 90, 110]
l.pop()
110
l.pop()
90
l.pop()
80
l.pop(3)
30
l
[10, 60, 70, 50, 40, 100, 120, 400]
l.pop(1)
60
l.remove(100)
l
[10, 70, 50, 40, 120, 400]
l.remove(400)
l
[10, 70, 50, 40, 120]
l
[10, 70, 50, 40, 120]
del l[l]
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    del l[l]
TypeError: list indices must be integers or slices, not list
del l[1]
l
[10, 50, 40, 120]
del l[2]
l
[10, 50, 120]
l.clear()
l
[]
id(l)
2931419827136
l=[200,30,33,42,10,70,50,40,100,120,400]
l
[200, 30, 33, 42, 10, 70, 50, 40, 100, 120, 400]
sorted(l)
[10, 30, 33, 40, 42, 50, 70, 100, 120, 200, 400]
l.sort()
l
[10, 30, 33, 40, 42, 50, 70, 100, 120, 200, 400]
min()
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    min()
TypeError: min expected at least 1 argument, got 0
min(l)
10
max(l)
400
sorted(l,reverse=True)
[400, 200, 120, 100, 70, 50, 42, 40, 33, 30, 10]
l
[10, 30, 33, 40, 42, 50, 70, 100, 120, 200, 400]
l.index(120)
8
>>> l.index(50)
5
>>> l.index(99)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    l.index(99)
ValueError: list.index(x): x not in list
>>> l.count(30)
1
>>> l.count(110)
0
>>> l.count(70)
1
>>> l
[10, 30, 33, 40, 42, 50, 70, 100, 120, 200, 400]
>>> m=l
>>> m
[10, 30, 33, 40, 42, 50, 70, 100, 120, 200, 400]
>>> m.append(700)
>>> m
[10, 30, 33, 40, 42, 50, 70, 100, 120, 200, 400, 700]
>>> l
[10, 30, 33, 40, 42, 50, 70, 100, 120, 200, 400, 700]
>>> n=l.copy()
>>> n
[10, 30, 33, 40, 42, 50, 70, 100, 120, 200, 400, 700]
>>> n.append(800)
>>> n
[10, 30, 33, 40, 42, 50, 70, 100, 120, 200, 400, 700, 800]
>>> l
[10, 30, 33, 40, 42, 50, 70, 100, 120, 200, 400, 700]
>>> len(l)
12
>>> sum(l)
1795
>>> # 0 0.0 ' '[] {} () set() False
>>> any
<built-in function any>
>>> any([1,2,3,4,5,6,7,8,9])
True
>>> all([1,2,3,4,5,6,7,8,9])
True
>>> all([1,2,3,4,5])
True
>>> all([8,5,34,5,6])
True
