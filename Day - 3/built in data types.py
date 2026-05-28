Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
========================================== RESTART: C:/Users/Ramakanth Reddy/OneDrive/Desktop/python-course-work/Day - 3/python data types.py ==========================================
hello
>>> a = 10
>>> type(a)
<class 'int'>
>>> t= 999.99
>>> type(t)
<class 'float'>
>>> c = 12+8j
>>> type(c)
<class 'complex'>
>>> s='python'
>>> type(s)
<class 'str'>
>>> s="dfghjkl"
>>> type(s)
<class 'str'>
>>> s='''sdfghjkl:'''
>>> type(s)
<class 'str'>
>>> l=[1,2,3,4]
>>> id(l)
3050153036864
>>> l=['post1.png','reel1.mp4']
>>> l
['post1.png', 'reel1.mp4']
>>> l=[]
>>> l=list()
>>> type(l)
<class 'list'>
>>> t=()
>>> t=(1,2,34,5,6,67)
>>> t
(1, 2, 34, 5, 6, 67)
>>> type(t)
<class 'tuple'>
s={1,2,3,4,6}
type(s)
<class 'set'>
s=set()
s={45678,546,3456,13423}
s
{3456, 546, 45678, 13423}
d ={'name':'abc','age':100,'course':'PFS'}
d
{'name': 'abc', 'age': 100, 'course': 'PFS'}
type(d)
<class 'dict'>
status =True
status =False
type(status)
<class 'bool'>
a= none
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a= none
NameError: name 'none' is not defined. Did you mean: 'None'?
type(a)
<class 'int'>
