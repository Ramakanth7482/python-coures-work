Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s=set()
s={1,11,1,1,1,1,1}
s
{1, 11}
s={987,654,345,56,345,1,2,34,6,56}
s
{1, 2, 34, 6, 654, 56, 345, 987}
s=set()
s
set()
s.add(1)
s
{1}
s.add(56.567)
s
{56.567, 1}
s.add("kjhl")
s
{56.567, 1, 'kjhl'}
s.add([1,2,3,3])
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s.add([1,2,3,3])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add((1,2,3,4))
s
{56.567, 1, (1, 2, 3, 4), 'kjhl'}
s.add({1,2,3,4})
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s.add({1,2,3,4})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
s
{56.567, 1, (1, 2, 3, 4), 'kjhl'}
1 in s
True
2 in s
False
False not in s
True
a= {1,2,3,5,6,8,10}
b= {6,7,8,9}
a | b
{1, 2, 3, 5, 6, 7, 8, 9, 10}
a.union(b)
{1, 2, 3, 5, 6, 7, 8, 9, 10}
a.intersection(b)
{8, 6}
a & b
{8, 6}
a - b
{1, 2, 3, 5, 10}
a ^ b
{1, 2, 3, 5, 7, 9, 10}
#{1} {2] {3}{5} {1,3} {1,2] {8,10}\

a <= {1}
False
a >= {1}
True
a <= {1,2,3,4,5,6,7,10,11,12}
False
a >= {6,10,8}
True
a
{1, 2, 3, 5, 6, 8, 10}
a.isdisjoint(b)
False
a.isdisjoint({90,80})
True
a
{1, 2, 3, 5, 6, 8, 10}
a.add(17)
a
{1, 2, 3, 17, 5, 6, 8, 10}
a.add(14)
a
{1, 2, 3, 5, 6, 8, 10, 14, 17}
a.update({11,12,13})
a
{1, 2, 3, 5, 6, 8, 10, 11, 12, 13, 14, 17}
a.pop()
1
a.pop()
2
a.remove(6)
a
{3, 5, 8, 10, 11, 12, 13, 14, 17}
a.remove(10)
a
{3, 5, 8, 11, 12, 13, 14, 17}
a.discard(6)
a
{3, 5, 8, 11, 12, 13, 14, 17}
a.discard(3)
a
{5, 8, 11, 12, 13, 14, 17}
a.discard(3)
a
{5, 8, 11, 12, 13, 14, 17}
>>> a={1,23,4,57,235}
>>> b={1,2,34,4}
>>> a.intersection(b)
{1, 4}
>>> a
{1, 4, 23, 57, 235}
>>> b
{1, 2, 4, 34}
>>> a.intersection_update(b)
>>> a
{1, 4}
>>> b
{1, 2, 4, 34}
>>> c=b
>>> c.add(12)
>>> c
{1, 2, 34, 4, 12}
>>> b
{1, 2, 34, 4, 12}
>>> d = c.cpoy()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    d = c.cpoy()
AttributeError: 'set' object has no attribute 'cpoy'
>>> d.add(10)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    d.add(10)
NameError: name 'd' is not defined. Did you mean: 'id'?
>>> d = c.copy()
>>> d.add(10)
>>> d
{1, 2, 34, 4, 10, 12}
>>> c
{1, 2, 34, 4, 12}
>>> len(c)
5
>>> min(c)
1
>>> max(c)
34
>>> sorted(c)
[1, 2, 4, 12, 34]
>>> sum(c)
53
