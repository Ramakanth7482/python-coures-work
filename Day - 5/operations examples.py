Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name = input()
ram
name
'ram'
name = input("Enter your name: ")
Enter your name:  vamsi
name
' vamsi'
age = input("Enter your age: ")
Enter your age: 21
age
'21'
type(age)
<class 'str'>
gpa = float(input("Enter the cpa: "))
Enter the cpa: 7.8
gpa
7.8
type(gpa)
<class 'float'>
'ram achy prak jash vamc'
'ram achy prak jash vamc'
'ram achy prak jash vamc'.split()
['ram', 'achy', 'prak', 'jash', 'vamc']
'java python c c++ javascrit'
'java python c c++ javascrit'
'java python c c++ javascrit'.split()
['java', 'python', 'c', 'c++', 'javascrit']
names = input("Enter the names: ").split()
Enter the names: ram achy prak jash vamc
names
['ram', 'achy', 'prak', 'jash', 'vamc']
products = input("Entre the products: ").split()
Entre the products: laptop mouse chaeger keyboard
products
['laptop', 'mouse', 'chaeger', 'keyboard']
topics = tuple(input("Enter the topics: ").split())
Enter the topics: token statement variable comments
topics
('token', 'statement', 'variable', 'comments')
marks
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    marks
NameError: name 'marks' is not defined. Did you mean: 'vars'?
marks = input("Enter the marks: ").split()
Enter the marks: 34 76 89 21 23
marks
['34', '76', '89', '21', '23']
int(['34','76','89','21','23'])
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    int(['34','76','89','21','23'])
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
map(int,input("Enter the marks: ").split())
Enter the marks: 5 6 7 9 0
<map object at 0x00000275A723BBC0>
list(map(int,input("Enter the marks: ").split()))
Enter the marks: 3 5 85 345
[3, 5, 85, 345]
prices = tuple(map(int,input("Enter the prices: ").split()))
Enter the prices: 4356 43567 456 8976 45 87
prices
(4356, 43567, 456, 8976, 45, 87)
rating = set(map(int,input("Enter the rating: ").split()))
Enter the rating: 4 3 4 5 3 3 2
rating
{2, 3, 4, 5}
per = list(map(float,input("Enter the per's : ").split()))
Enter the per's : 56.3 23.3 78.9 34.5
per
[56.3, 23.3, 78.9, 34.5]
prices = tuple(map(float,input("Enter the prices: ").split()))
Enter the prices: 567 4567 45678 5678 45367 45
prices
(567.0, 4567.0, 45678.0, 5678.0, 45367.0, 45.0)
prices = set(map(float,input("Enter the prices: ").split()))
Enter the prices: 5467 34567 5467 54678 65
prices
{65.0, 5467.0, 54678.0, 34567.0}
a,b = 10,20
a
10
b
20
a,b = (10,20)
a
10
b
20
a,b=[10,20]
a
10
b
20
username,password = input("Enter thr username & password: ").split()
Enter thr username & password: codegnan r@123
username
'codegnan'
password
'r@123'
a,b,c,d = list(map(int,input("Enter the 4 sides: ").split()))
Enter the 4 sides: 8 5 5 8
a
8
b
5
c
5
d
8
price,discount = list(map(float,input().split()))
375850 89.0
price
375850.0
discount
89.0
a= eval(input())
a
a= eval(input())
34567
a
34567
a= eval(input())
4567.54678
a
4567.54678
a= eval(input())
[1,2,3,4,4]
a
[1, 2, 3, 4, 4]
a= eval(input())
(1,2,3,4)
a
(1, 2, 3, 4)
a= eval(input())
{1,2,3,4,5}
a
{1, 2, 3, 4, 5}
a= eval(input())
True
a
True
type(a)
<class 'bool'>
s='python programming lang'
s
'python programming lang'
type(S)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    type(S)
NameError: name 'S' is not defined. Did you mean: 's'?
type(s)
<class 'str'>
s=''
s
''
a='codegnan'
b='pfs'
a+b
'codegnanpfs'
a*10
'codegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnan'
'*'*20
'********************'
'python '*6
'python python python python python python '
names = 'ram achy prak jash vamc'
names
'ram achy prak jash vamc'
>>> names[5]
'c'
>>> names [10]
'r'
>>> names
'ram achy prak jash vamc'
>>> names[-4]
'v'
>>> names[-6]
'h'
>>> names
'ram achy prak jash vamc'
>>> names[:3]
'ram'
>>> names[:4:8]
'r'
>>> name[4:8]
'si'
>>> names
'ram achy prak jash vamc'
>>> names[-4]
'v'
>>> names[-4:]
'vamc'
>>> names[-8:-6]
'as'
>>> names[4::-1]
'a mar'
>>> names[8:-1]
' prak jash vam'
>>> names[8::-1]
' yhca mar'
>>> names[::-1]
'cmav hsaj karp yhca mar'
>>> 'ram' in names
True
>>> 'naresh' not in names
True
>>> max(names)
'y'
>>> min(names)
' '
>>> sorted(names)
[' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'c', 'c', 'h', 'h', 'j', 'k', 'm', 'm', 'p', 'r', 'r', 's', 'v', 'y']
