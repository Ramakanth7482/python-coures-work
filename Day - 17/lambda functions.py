'''Lambda Function in Python

A lambda function is a small anonymous (nameless)
function that can have any number of arguments but only one expression


Advantages

Short and concise code.
Useful for simple functions.
Commonly used with map(), filter(), and sorted().

syntax:
var = lambda agr: exp
add = lambda a,b: a+b

print(add(12,13))
print(add(22,33))



wish = lambda name: f'Welcome the python course {name}'
print(wish('ram'))
print(wish('achy'))



gst = lambda price:price + price*0.18

print(gst(1000))
print(gst(600))
print(gst(89000))





greatest = lambda a,b: a if a>b else b

print(greatest(18,19))
print(greatest(2000,1900))
print(greatest(10,30))


iseven = lambda a: f"{a}-Even number" if a%2==0 else f"{a}-odd number"

print(iseven (4))
print(iseven (9))
print(iseven (65))



bill = lambda charge: charge if charge>99 else charge + 30
print(bill(150))
print(bill(45))
print(bill(15))



login = True
instock = False

status = lambda login,instock :("You can buy product" if instock else "Product is out of stock") if login else "Login to buy a product"

print(status(login,instock))





d = {'sugar':40,'salt':20,'milk':50,'cooking oil':90}
for i in d:
    d[i] += d[i]*0.18

print(d)




l=[1,2,3,4,5,6,7]
res = list(map(lambda i:i**3,l))
print(res)


names = ['ram','achy','prak']
t = list(map(lambda i:i.title(),names))
print(t)



l =[1,2,3,4,5,6,7]
res = list(filter(lambda i:i%2==0,l))
print(res)



l =[1,2,3,4,5,6,7]
res = list(filter(lambda i:i>5,l))
print(res)




l =[1,2,3,4,5,6,7]
res = list(filter(lambda i:i%3==0,l))
print(res)




from functools import reduce

l=[1,2,3,4,5,6,7,8,9,10,11,12,]

s = reduce(lambda sum,i: sum+i,l)
p = reduce(lambda pro,i: pro*i,l)

print(s,p)




from functools import reduce

l=[1,2,3,4,5,6,7,8,9,10,11,12,]

s = reduce(lambda sum,i: sum+i,l)
p = reduce(lambda pro,i: pro*i,l)
m = reduce(lambda max,i: max if max>i else i,l)
mi = reduce (lambda max,i: max if max<i else i,l)

print(s,p,m,mi)




d = {'ram':50,'achy':40,'prakesh':60,'naresh':70,'vamc':80}

print(dict(sorted(d.items())))
print(dict(sorted(d.items(),key=lambda i:i[1])))

print(dict(sorted(d.items(),reverse= True)))
print(dict(sorted(d.items(),key=lambda i:i[1],reverse= True)))
'''




























