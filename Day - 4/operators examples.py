Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=20
b=10
a+b
30
a-b
10
a*b
200
a/b
2.0
9/2
4.5
9//2
4
a**2
400
6**3
216
a%b
0
17%4
1
17%3
2
a
20
b
10
a<b
False
a>b
True
a<=b
False
10<=b
True
a>=b
True
a==b
False
a!=b
True
y = 5
y
5
y=y+10
y
15
y=y+15
y
30
y+=10
y
40
y+=10
y
50
y+=10
/
SyntaxError: invalid syntax
\
  y+=10
SyntaxError: unexpected indent
y+=10
\

  \
\

y = 5
y
5
y=y
y=y+10
y
15
y%=2
y
1
y+=10
y
11
y/=2
y
5.5
y
5.5
a%10==10
False
a%10==0
True
a%20==0 and b%20==0 and a>b
False
a%20==0 or b%20==0 or a>b
True
a%20==0 or b%20==0 or a<b
True
a%20==0 or b%20==0 or a<b
True
not a>b
False
#str,list,tuple,set,dict
a ='python programming'
a
'python programming'
'y' in a
True
'g' in a
True
'z' not in a
True
'r' not in a
False
l=['java','python','mysql','c++','html']
'mysql' in l
True
'javascript' in l
False
'c' not in ;
SyntaxError: invalid syntax
'c' not in l
True
t ('loptop','mobile','mouse','keyboard')
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    t ('loptop','mobile','mouse','keyboard')
NameError: name 't' is not defined
t=('loptop','mobile','mouse','keyboard')
t
('loptop', 'mobile', 'mouse', 'keyboard')
'charger' in t
False
'laptop' in t
False
t = {1,2,4,56,78,235,23}
t
{1, 2, 4, 23, 56, 235, 78}
4 in t
True
50 not in t
True
d={'egg':8,'oil':120,'sugar':40,'sail':30}
'oil' in d
True
120 in d
False
'sugar' in d
True
'chilli' in d
False
l=[1,2,3,4,5]
m=[1,2,3,4,5]
l==m
True

n=m
n
[1, 2, 3, 4, 5]
n==m
True
l is m
False
n is m
True
id(l)
1800956048384
id(m)
1800956047296
id(n)
1800956047296
l is m
False
n is m
True
8 & 14
8
8 & 7
0
8 | 7
15
10^11
1
~12
-13
~15
-16
>>> ~19
-20
>>> ~70
-71
>>> 8>>2
2
>>> 15>>1
7
>>> 15>>3
1
>>> 15>>2
3
>>> 16<<1
32
>>> 4<<2
16
>>> a= 12
>>> b=12.34
>>> c='python'
>>> print(a,b,c)
12 12.34 python
>>> print("a=",a,'b=',b, 'c=',c)
a= 12 b= 12.34 c= python
>>> print("a=",a,'b=',b, 'c=',c,sep='')
a=12b=12.34c=python
>>> print("a=",a,'b=',b, 'c=',c,sep='\n')
a=
12
b=
12.34
c=
python
>>> print("a=",a,'b=',b, 'c=',c,sep='',end='\n\n')
a=12b=12.34c=python

>>> print("a=",a,'b=',b, 'c=',c,sep='',end='@@@')
a=12b=12.34c=python@@@
>>> print(f'a= {a} b={b} c={c}')
a= 12 b=12.34 c=python
>>> print('a= %d b=%.2f c=%s'%(a,b,c))
a= 12 b=12.34 c=python
>>> print('a= {} b= {} c={}'.format(a,b,c))
a= 12 b= 12.34 c=python
>>> print('a= {2} b= {0} c={1}'.format(a,b,c))
a= python b= 12 c=12.34
