'''
#local accesses

def display():
    n=10
    print("Inside:",n)

display()
print("Outside:",n)



#global accesses

n=10
def display():
    print("Inside:",n)

display()
print("Outside:",n)


# global n = outside outprint will  also come

def display():
    global n
    n=10
    print("Inside:",n)

display()
print("Outside:",n)



# glabel keyword

def display():
    global n
    n+=10
    print("Inside:",n)
    
n=10
display()
print("Outside:",n)



def display(n):
    #global n
    n+=10
    print("Inside:",n)
    
n=10
display(n)
print("Outside:",n)



def display():
    n=10
    def inner(n):
        n+=10
        print("Inner function:",n)
    inner(n)

    print("Outer function:",n)

display()



#nonlocal

def display():
    n=10
    def inner():
        nonlocal n
        n+=10
        print("Inner function:",n)
    inner()

    print("Outer function:",n)

display()



s='python'
print(len(s))

len=5
print(len(s))



#int float complex str list tuple set dict bool -> data types
#int float complex str tuple bool -> inside and outsude are not same
#list set dict -> inside and outside same


#int

def update(n):
    n+=10
    print("Inside:",n)

n=10.4
update(n)
print("Outside:",n)


#float

def update(n):
    n+=10
    print("Inside:",n)

n=10
update(n)
print("Outside:",n)


#complex
def update(n):
    n+=10
    print("Inside:",n)

n=3+4j
update(n)
print("Outside:",n)


#list
def update(n):
    n=[6]
    print("Inside:",n)

n=[1,2,3,4,5]
update(n)
print("Outside:",n)



#tuple

def update(n):
    n+=(6,9)
    print("Inside:",n)

n=(1,2,3)
update(n)
print("Outside:",n)



#set

def update(n):
    n.add(6)
    print("Inside:",n)

n={1,2,3}
update(n)
print("Outside:",n)


#bool

def update(n):
    n=False
    print("Inside:",n)

n=True
update(n)
print("Outside:",n)
'''


#dict

def update(d):
    d['course']='python'
    print('inside:',d)

d={'name':'ram'}
update(d)
print('outside',d)




















































