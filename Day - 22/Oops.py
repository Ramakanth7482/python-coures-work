'''
#Oops:-
=> OOPS (Object-Oriented Programming System) in Python is a
programming paradigm thatorganizes code using objects and classes.

=> OOPS (Object-Oriented Programming System) is a programming paradigm
that uses classes and objects to structure programs, making code reusable,
maintainable, and scalable.


#Class and Object:-
=> Class: Blueprint for creating objects.
=> Object: Instance of a class.

#Four Pillars of OOP:-
1.Encapsulation – Bundling data and methods together.
2.Inheritance – Creating a new class from an existing class.
3.Polymorphism – Same method name, different behavior.
4.Abstraction – Hiding implementation details.




#Encapsulation in Python:-
=> Encapsulation is the process of wrapping data (variables)
and methods (functions) into a single unit (class) and
restricting direct access to some data.


#Inheritance in Python:-
=> Inheritance is a feature of OOP that allows one class (child class)
to inherit the properties and methods of another class (parent class).


#Polymorphism in Python:-
=> Polymorphism means "many forms." It allows the same method or
function name to behave differently for different objects.


#Abstraction in Python:-
=> Abstraction means hiding the internal implementation details
and showing only the essential features to the user.




class Flipkart:
    pass

ram = Flipkart()
achyuth = Flipkart()
vamsi = Flipkart()




class Flipkart:
    discount = 10
    products = ['laptop','phone','mouse','charger']

    @classmethod
    def showproducts(cls):
        print(cls.products)

    def login(self,username,password):
        self.username = username
        self.password = password
        print(f'welcome to the flipkart {self.username}')

    @staticmethod
    def banner():
        print("10% discount is going on flipkart, shop now!")

ram = Flipkart()
ram.login('ram','ram2003@')
ram.banner()
ram.showproducts()

Flipkart.showproducts()
Flipkart.banner()



# changing the username:-

class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.followers = []
        print(f'Welcome to the Instagram,{self.username}')

vamsi = Instagram('vamsi','vamsi@123')

print("Before usrename:",vamsi.username)
vamsi.username = 'ram'
print("After username:",vamsi.username)
'''


class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self.followers = []

    def getpassword(self):
        return self.__password

    def setpassword(self,newpassword):
        self.__password = newpassword

vamsi = Instagram('vamsi','vamsi@123')

print("Before usrename:",vamsi.username)
vamsi.username = 'ram'
print("After username:",vamsi.username)

print("Before password:",vamsi.getpassword())
vamsi.setpassword('ram@123')
print("After password:",vamsi.getpassword())













































