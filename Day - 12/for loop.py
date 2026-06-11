'''seq: str,list,tuple,set,dict,range
for i in seq:
    print(i)


pin = 7482
for i in range(5):
    e_pin = int(input("Enter the pin: "))
    if e_pin == pin:
        print("Unlock the phone")
        break
    else:
        print("incorrect pin")
else:
    print("Try again,after 60 seconds")



l=[2,3,5,6,8,10,34,12]
search = int(input("Enter the element: "))

for i in range(len(l)):
    if l[i]== search:
        print(f'{search} is found at index-{i}')
        break
else:
    print(f'{search} is not found')




password = input("Enter the password: ")
if len(password)>=8:
    s = set()
    for i in password:
        if i.isupper():
            s.add('u')
        elif i.islower():
            s.add('l')
        elif i.isdigit():
            s.add('d')
        else:
            s.add('s')

    if len(s)==4:
        print("is a strong password")
    else:
        print("Not a strong password")
else:
    print("weak password")




status = True
assert status != None, "You need to update the status"
print(status)



name = 'ram'
batch = 55
age = 21
assert (name!=None and batch!=None and age!=None), "You need to update the status"
print(name,batch,age)
'''
            
            
