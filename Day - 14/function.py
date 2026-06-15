'''1. reuse
2. modul
3. deb
4. readabuality
5. maintabulity



built functions:-


| Function   | Description             | Example                         |
| ---------- | ----------------------- | ------------------------------- |
| `print()`  | Displays output         | `print("Hello")`                |
| `input()`  | Takes user input        | `name = input()`                |
| `len()`    | Returns length          | `len("Python")` → `6`           |
| `type()`   | Returns data type       | `type(10)` → `<class 'int'>`    |
| `int()`    | Converts to integer     | `int("5")` → `5`                |
| `float()`  | Converts to float       | `float("5.5")` → `5.5`          |
| `str()`    | Converts to string      | `str(10)` → `"10"`              |
| `list()`   | Creates a list          | `list("abc")` → `['a','b','c']` |
| `sum()`    | Returns sum of elements | `sum([1,2,3])` → `6`            |
| `max()`    | Returns largest value   | `max(1,5,3)` → `5`              |
| `min()`    | Returns smallest value  | `min(1,5,3)` → `1`              |
| `sorted()` | Sorts elements          | `sorted([3,1,2])` → `[1,2,3]`   |
| `abs()`    | Returns absolute value  | `abs(-10)` → `10`               |
| `round()`  | Rounds a number         | `round(3.75)` → `4`             |




def function_name(arg):
    #stmts
    return
function_name(para)



def wish(name):
    print(f' Wellcome to the python course {name} !')

wish('ram')
wish('achy')
wish('vamc')
wish('jassu')
wish('prakesh')


def iseven(num):
    if num%2==0:
        return f"{num} - Even number"
    else:
        return f"{num} - Odd Number"

print(iseven(12))
print(iseven(13))


def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *=i
    return fact

num = int(input("Enter the numbre: "))
print(factorial(num))



def isprime(num):
    for i in range(2,num//2):
        if num%i==0:
            return f"{num} - Not Prime number"

    return f"{num} - Prime Number"

num = int(input("Enter the number: "))
print(isprime(num))
'''          
        














