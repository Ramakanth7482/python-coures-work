'''
1. posistion
2. keyword
3. default
4. variable


def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("password:",pwd)

display('ram','ram@7482gmail.com','ram123')
display('ram@7482gmail.com','ram123','ram')
display('ram123','ram','ram@7482gmail.com')


def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("password:",pwd)

display(name='ram',email='ram@7482gmail.com',pwd='ram123')
display(email='ram@7482gmail.com',pwd='ram123',name='ram')
display(pwd='ram123',name='ram',email='ram@7482gmail.com')



def display(name,email,pwd=''):
    print("Name:",name)
    print("Email:",email)
    print("password:",pwd)

display('ram','ram@7482gmail.com','ram123')
display('ram','ram@7482gmail.com')



def display(*names):
    print("Names:",names)

display('ram','vamc','achy','prakesh','jassu')
display('ram','vamc','achy','prakesh')
display('ram','vamc','achy')
display('ram','vamc')
display('ram')
'''


def display(**names):
    print("Names:",names)

display(k1='ram',k2='vamc',k3='achy',k4='prakesh',k5='jassu')
display(k1='ram',k2='vamc')
display(k1='ram',k2='vamc',k3='achy')


