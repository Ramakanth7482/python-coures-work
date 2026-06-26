'''
#non premiumHotstar:-

class Hotstar:
    def __init__(self,name):
        self.name = name
        print(f"Hi {self.name}, Welcome to the hotstar")
    def login(self):
        print("You can login")
    def dashboard(self):
        print("You can see the dashboard items")
    def search(self):
        print("You can search")
    def languages(self):
        print("You can select the languages")
    def playcontrollers(self):
        print("You can pause and play the video")
    def ads(self):
        print("Ads will run")
    def movies(self):
        print("You can limited access for movies")
    def sports(self):
        print("Limited time you can watch sports")
    def quality(self):
        print("limited quality")

ram = Hotstar('ram')
ram.login()
ram.dashboard()
ram.search()
ram.languages()
ram.playcontrollers()
ram.ads()
ram.movies()
ram.sports()
ram.quality()


# PremiumHotstar:-

class PremiumHotstar:
    def __init__(self,name):
        self.name = name
        print(f"Hi {self.name}, Welcome to the hotstar")
    def ads(self):
        print("Ads won't run")
    def movies(self):
        print("You can unlimited access for movies")
    def sports(self):
        print("You can watch sports")
    def quality(self):
        print("High quality")

ramakanth = PremiumHotstar('ramakanth')
ramakanth.ads()
ramakanth.movies()
ramakanth.sports()
ramakanth.quality()


#Overlooding:-

class Number:
    def __init__(self,n):
        self.n = n
    def __add__(self,other):
        return self.n + other.n
    def __sub__(self,other):
        return self.n - other.n
    def __mul__(self,other):
        return self.n * other.n
    def __truediv__(self,other):
        return self.n / other.n
    def __eq__(self,other):
        return self.n == other.n
    def __it__(self,other):
        return self.n < other.n
    def __gt__(self,other):
        return self.n > other.n
    def __str__(self):
        return str(self.n)

n1 = Number(10)
n2 = Number(20)
print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)
print(n1==n2)
print(n1<n2)
print(n1>n2)
print(n1,n2)


#Book Details Display:-

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")
Price: ("${self.price}")

book1 = Book("Clean Code", "Robert Martin", 450)
book1.display_info()

#Employee Salary Calculator:-

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary


    def calculate_annual_salary(self):
        return self.base_salary * 12

# Object creation
emp = Employee("John", 35000)
print("Annual Salary:", emp.calculate_annual_salary())



#Student Grade Evaluator:-

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def is_passed(self):
        avg = sum(self.marks) / len(self.marks)
        return avg >= 40

s1 = Student("Priya", [45, 56, 60])
print("Passed:", s1.is_passed())



#Bank Account Simulation:-


class BankAccount:


    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(f"Balance: {self.balance}")

# Use case
acc = BankAccount("Arjun")
acc.deposit(1000)
acc.withdraw(500)
acc.show_balance()


#Car Odometer:-

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.odometer = 0
    def drive(self, km):
        self.odometer += km


    def show_odometer(self):
        print(f"Odometer: {self.odometer} km")

# Create object
car1 = Car("Toyota", "Innova")
car1.drive(120)
car1.drive(30)
car1.show_odometer()
'''


#Movie Rating Check:-

class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating
    def is_family_friendly(self):
        return self.rating < 13

# Use case
m1 = Movie("Finding Nemo", "Animation", 8)
print("Family Friendly:", m1.is_family_friendly())
























































































    































    





































































































































