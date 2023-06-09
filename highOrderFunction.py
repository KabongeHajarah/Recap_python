def sum_numbers(nums):
 return sum(nums)

def higher_order_function(f,lst):
 summation=f(lst)
 return summation
result=higher_order_function(sum_numbers,[1,2,3,4])
print(result)

#Function as a return value
def square(x):       
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3

#Python Closures
#Python allows a nested function to access the outer scope of the enclosing function. This is is known as a Closure. 
def add_ten():
   ten=10
   def add(num):
      return num+ten
   return add

closure_result=add_ten()
print(closure_result(5))
print(closure_result(10))

#A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. 
# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## Let us implement the example above with a decorator

'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON
