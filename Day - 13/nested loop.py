'''s='python'

for i in range(len(s)):
    for j in range(i+1,len(s)):
        print(s[i],s[j],sep='',end=' ')



l=[1,2,3],[4,5,6],[7,8,9]
sum = 0
for i in l:
    for j in i:
        sum+=j

print(f'sum = {sum}')




d={
    '1234':{'pin':'4567','balamce':2300},
    '2345':{'pin':'9876','balamce':5300},
    '3456':{'pin':'5678','balamce':6300},
    '4567':{'pin':'9867','balamce':7300}

   }

for i in d:
    print('Account number:',i)
    print('pin number:',d[i]['pin'])



for i in range(8):
    for j in range(2):
        print(i,end=' ')
        print()
        



n = int(input())
for row in range(n):
    for col in range(n):
        print(col % 2, end=" ")
    print()

#
01010
01010
01010
01010
01010


for row in range(9):
    for col in range(row+1):
        print('*',end=' ')
    print()

#
*
**
***
****
*****

n = int(input())
for i in range(n):
    for j in range(n-i):
        print('*',end=' ')
    print()

#
*****
****
***
**
*



n= int(input("Enter the size: "))
for row in range(n):
    for sp in range(row):
        print(' ',end=' ')
    for col in range(n-row):
        print('*',end=' ')
    print()

#
*******
 ******
   ****
    ***
     **
      *



n = int(input())
for i in range(n):
    for j in range(n):
        print((i+j)%2,end=" ")
    print()
#
01010
10101
01010
10101
01010
'''
n= int(input('Enter the size: '))
c=1
for row in range(n):
    for col in range(row+1):
        print(str(c).zfill(2),end=' ')
        c+=1
    print()


'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''

 






 
