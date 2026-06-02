Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='python programming'
s
'python programming'
s.replace('python','java')
'java programming'
s.maketrans('python','123456')
{112: 49, 121: 50, 116: 51, 104: 52, 111: 53, 110: 54}
s.translate(s.maketrans('python','123456'))
'123456 1r5grammi6g'



splitting and joining methods
SyntaxError: invalid syntax

splitting and joining methods
SyntaxError: invalid syntax
s='java,python,javascript,c,c++'
s.split(',')
['java', 'python', 'javascript', 'c', 'c++']
>>> s.split(',',2)
['java', 'python', 'javascript,c,c++']
>>> s.rsplit(',',2)
['java,python,javascript', 'c', 'c++']
>>> g='sdfgh'
>>> g='''dsfghjk'''
>>> g='''dfghjk'''
>>> 
...  
>>> g
'dfghjk'
>>> s.splitlines()
['java,python,javascript,c,c++']
>>> l=['java,python,javascript,c,c++']
>>> g.splitlines()
['dfghjk']
>>> s.splitlines()
['java,python,javascript,c,c++']
>>> g='''dfghjk'''S
SyntaxError: invalid syntax
>>> ','join(1)
SyntaxError: invalid syntax
>>> ''.join(1)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    ''.join(1)
TypeError: can only join an iterable
>>> s.partition(',')
('java', ',', 'python,javascript,c,c++')
>>> s.rpartition(',')
('java,python,javascript,c', ',', 'c++')
>>> 
>>> 
>>> 
>>> t ="Hello 🙂"
>>> t.encode()
b'Hello \xf0\x9f\x99\x82'
>>> b'Hello \xf0\x9f\x99\x82'.decode()
'Hello 🙂'
