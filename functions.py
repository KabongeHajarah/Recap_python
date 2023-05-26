# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers (num1, num2):
    sum=num1 +num2
    return sum 
print(add_two_numbers(10,20))
print(add_two_numbers(1,2))

# Area of a circle is calculated as follows: area = π x r x r. 
# Write a function that calculates area_of_circle.
import math
def area_of_circle (pie,radius):
    area= pie * radius* radius
    return area
print(area_of_circle(math.pi, 10))

# Write a function called add_all_nums 
# which takes arbitrary number of arguments and sums all the arguments.
#  Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    total=0
    for num in args:
        if isinstance (num,(int,float)):
            total+=num
        else: 

            return "Error:All arguments must be numeric"
    return total
    
print(add_all_nums(10,20,345,20.34,290.567))
print(add_all_nums(10,20,345,True,"Bellah"))

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
#  Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperature_fahrenheit = convert_celsius_to_fahrenheit(20)
print(temperature_fahrenheit)  # Output: 68.0
 
# Write a function called check-season, 
# it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
     if month in [3, 4, 5]:     #we put the months in a range e.g(march,april, may)
        return "Spring"
     elif month in [6, 7, 8]:
        return "Summer"
     elif month in [9, 10, 11]:
        return "Autumn"
     elif month in [12, 1, 2]:
        return "Winter"
     else:
        return "Invalid month"


season = check_season(6)
print(season) 
print(check_season(13))


# Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope

# Example usage:
x1 = 2
y1 = 4
x2 = 6
y2 = 10

slope = calculate_slope(x1, y1, x2, y2)
print(slope)  # Output: 1.5

# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
# Declare a function named print_list.
#  It takes a list as a parameter and it prints out each element of the list.
def print_list(names):
    for name in names:
        print(name)
print_list(["Bellah","Mlaeek","Shaturah"])
    
# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(array):
    reversed_array = []
    for i in range(len(array) - 1, -1, -1):
        reversed_array.append(array[i])
    return reversed_array

# Example usage:
my_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(my_list)
print(reverse_list(["A", "B", "C"]))
print(reversed_list)

# # [5, 4, 3, 2, 1]

# # ["C", "B", "A"]
# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# numbers = [2, 3, 7, 9];
# print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9];
# print(remove_item(numbers, 3))  # [2, 7, 9]
# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def  sum_of_numbers(numbers):
    sum=0
    for num in numbers:
            sum+=num
    return sum
print(sum_of_numbers(range(5)))
print(sum_of_numbers(range(101)))


# Declare a function named sum_of_odds. 
# It takes a number parameter and it adds all the odd numbers in that range.
def  sum_of_odds(numbers):
      
    sum=0
    for num in numbers:
        if num%2!=0:
            sum+=num
    return sum
print(sum_of_odds(range(100)))
print(sum_of_odds(range(10)))


# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def  sum_of_even(numbers):
      
    sum=0
    for num in numbers:
        if num%2==0:
            sum+=num
    return sum
print(sum_of_even(range(100)))
print(sum_of_even(range(10)))