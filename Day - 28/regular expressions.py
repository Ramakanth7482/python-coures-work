'''
import re

pattern = r'h.t\b'
text = 'hot hit het hrt hat hood heart hjt h$t'

res = re.findall(pattern,text)
print(res)




import re

pattern = r'^h'
text = 'uot hit het hrt hat hood heart hjt h$t'

res = re.findall(pattern,text)
print(res)



import re

pattern = r't$'
text = 'hot hit het hrt hat hood heart hjt h$t'

res = re.findall(pattern,text)
print(res)



import re

pattern = r'to?\b'
text = 'too to t tooooooo toooooooooo'

res = re.findall(pattern,text)
print(res)


import re

pattern = r'[a-z]{4,5}'
text = 'serdfgh fghj fghj ghjkl ghjkk'

res = re.findall(pattern,text)
print(res)


import re

pattern = r'(pyton)'
text = 'pyth pythn python puthon'

res = re.findall(pattern,text)
print(res)



import re

pattern = r'^[a-zA-Z]{2,15}( [a-zA-Z] {2,15})+$'
text = input("Enter the name: ")

res = re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid format")





import re

pattern = r'^(?:\+91|0)?[6-9]\d{9}$'
text = input("Enter the number: ")

res = re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid format")





import re

pattern = r'[a-zA-Z0-9@$%^&]{8,}'
text = input("Enter the text: ")

res = re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid format")



import re

pattern = r'^(?=.*[A-Z]) (?=.*[a-z]) (?=.*\d) (?=.*[@$!%*?&]) [A-Za-z\d@$!%*?&]{8,}'
text = input("Enter the text: ")

res = re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid format")




import re

pattern = r'^[a-zA-Z0-9_]{5,15}$'
text = input("Enter the text: ")

res = re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid format")




import os

os.mkdir("sample")


#os.rmdir("sample")



import os

#os.mkdir("sample")
os.makedirs('sample/demo')

#os.rmdir("sample")



import os

#os.mkdir("sample")
#os.makedirs('sample/demo')

path = os.path.join('sample/demo','demo.txt')
with open(path,'w+') as file:
    file.write("Hello worid")
    file.seek(0)
    print(file.read())
#os.rmdir("sample")
'''


import os
import shutil

'''print(os.listdir('.'))
os.chdir('../')
print(os.listdir('.'))
'''
print(os.path.abspath('main.py'))
print(os.path.exists('main.py'))
print(os.path.getsize('main.py'))

#shutil.rmtree('sample')

#os.mkdir("sample")
#os.makedirs('sample/demo')
'''
path = os.path.join('sample/demo','demo.txt')
with open(path,'w+') as file:
    file.write("Hello worid")
    file.seek(0)
    print(file.read())
    '''
#os.rmdir("sample")


