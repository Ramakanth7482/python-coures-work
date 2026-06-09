#bonus
'''
a=int(input())
if a>= 70000:
    print("bonus:",a*0.2)
elif a>= 50000:
    print("bonus:",a*0.15)
elif a>=30000:
    print("bonus:",a*0.10)
else:
    print("bonus:",a*0.05)
'''
tup= tuple(input("tuple :").split())
pro = input("product: ")
pri = int(input("price: "))
s =set(map(int,input("set values : ").split()))
print("tuple:",tup)
d={}
d[pro]=pri
print("dictinory: ",d)
print("set:",s)
