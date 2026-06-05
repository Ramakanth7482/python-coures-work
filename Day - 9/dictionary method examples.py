Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d={}
d=dict()
type(d)
<class 'dict'>
d={'k1':'v1','k2':'v2'}
d
{'k1': 'v1', 'k2': 'v2'}
d={]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
d={}
d[1]='int'
d
{1: 'int'}
d[12.3]='float'
d
{1: 'int', 12.3: 'float'}
d['demo']='str'
d
{1: 'int', 12.3: 'float', 'demo': 'str'}
d[2+3j]='complex'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex'}
d[[1,2,3,4]]='list'
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    d[[1,2,3,4]]='list'
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex'}
d[False]='bool'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex', False: 'bool'}
d={}
d[1]=1
d
{1: 1}
d[23]=23.4
d[3]='fdghjk'
d[4]=3+4j
d[5]=[1,2,3]
d[6]=(1,2,3)
d[7]={1,3}
d[8]={1:1,2:2}
d[9]=False
d
{1: 1, 23: 23.4, 3: 'fdghjk', 4: (3+4j), 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 3}, 8: {1: 1, 2: 2}, 9: False}
d={}
d
{}
d={}d[1]=2
SyntaxError: invalid syntax
d={}
d[1]=2
d[2]=2
d[3]=2
d[4]=2
d
{1: 2, 2: 2, 3: 2, 4: 2}
d[3]
2
d={1: 2, 2: 2, 3: 2, 4: 2}
d
{1: 2, 2: 2, 3: 2, 4: 2}
d[2]
2
d[4]
2
d[6]
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    d[6]
KeyError: 6
d[3]
2
d={'ram':89,'achyuth':76,'jassu':90,'prakesh':98,'vamshi':95}
d['ram']
89
d['jassu']
90
d['vamshi']
95
d['naresh']
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    d['naresh']
KeyError: 'naresh'
d.get('naresh')
d.get('achyuth')
76
d.get('rama','user not found')
'user not found'
d.get('prakesh','user not found')
98
d
{'ram': 89, 'achyuth': 76, 'jassu': 90, 'prakesh': 98, 'vamshi': 95}
'ram' in d
True
'achyuth' in d
True
d.keys()
dict_keys(['ram', 'achyuth', 'jassu', 'prakesh', 'vamshi'])
d.values()
dict_values([89, 76, 90, 98, 95])
d.items()
dict_items([('ram', 89), ('achyuth', 76), ('jassu', 90), ('prakesh', 98), ('vamshi', 95)])
sorted(d)
['achyuth', 'jassu', 'prakesh', 'ram', 'vamshi']
min(d)
'achyuth'
max(d)
'vamshi'
len(d)
5
d
{'ram': 89, 'achyuth': 76, 'jassu': 90, 'prakesh': 98, 'vamshi': 95}
d['ram']
89
d['ram']=100
d
{'ram': 100, 'achyuth': 76, 'jassu': 90, 'prakesh': 98, 'vamshi': 95}
d['achyuth'=50
  
SyntaxError: '[' was never closed
d['achyuth']=50
  
d
  
{'ram': 100, 'achyuth': 50, 'jassu': 90, 'prakesh': 98, 'vamshi': 95}
d['achyth']=50
  

d.update({'praneeth':92,'naresh':99})
  
d
  
{'ram': 100, 'achyuth': 50, 'jassu': 90, 'prakesh': 98, 'vamshi': 95, 'achyth': 50, 'praneeth': 92, 'naresh': 99}
>>> d.pop()
...   
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 argument, got 0
>>> d.popitem()
...   
('naresh', 99)
>>> d
...   
{'ram': 100, 'achyuth': 50, 'jassu': 90, 'prakesh': 98, 'vamshi': 95, 'achyth': 50, 'praneeth': 92}
>>> del d['jassu']
...   
>>> d
...   
{'ram': 100, 'achyuth': 50, 'prakesh': 98, 'vamshi': 95, 'achyth': 50, 'praneeth': 92}
>>> d.clear()
...   
>>> d
...   
{}
>>> d.setdefault('vamshi',0)
...   
0
>>> d
...   
{'vamshi': 0}
>>> d
...   
{'vamshi': 0}
>>> d.setdefault('satish',87
...              d
...              
SyntaxError: '(' was never closed
>>> d
...              
{'vamshi': 0}
>>> d={'ram': 100, 'achyuth': 50, 'jassu': 90, 'prakesh': 98, 'vamshi': 95, 'achyth': 50, 'praneeth': 92}
... d
...              
SyntaxError: multiple statements found while compiling a single statement
