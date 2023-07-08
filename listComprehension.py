#Is the compact way of creating a list from a sequence
# One way
language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst) 

#Secondway: List comprehension
lst=[i for i in language]
print(type(lst))
print(lst)

numbers=[i for i in range(21)]
print(numbers)
print(numbers *2)  #print it twice
 #tuples
nums=[(i,i*i) for i in range (11)]
print(nums)

# Can be combined with if statements
#even numbers generation
even_numbers=[i for i in range(101) if i%2==0 ]
print(even_numbers)

#Filter even positive numbers 
numbers=[-8,-2,-2,1,2,3]
postive_even=[i for i in numbers if i%2==0 and  i>0]
print(postive_even)

#Flattening a three dimensional array--making it one 
list_of_lists=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list=[number for row in list_of_lists for number in row ]
print(flattened_list)

#Lambda Function--is a small anonymous function without a name
add_two_numbers= lambda a,b:a+b
print(add_two_numbers(10,20))

# Self invoking lambda function
print((lambda a, b: a + b)(2,3)) 


# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22

#Lambda Function inside another function 
def power (x):
    return lambda n: (n**x)
cube =power(2)(3)
print(cube)


#EXERCISES
# 1.Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_zer0=[i for i in numbers if i<=0]
print(negative_zer0)

#Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list=[num for row in list_of_lists for row in row for num in row ]
print(flattened_list)
              

#Using list comprehension create the following list of tuples:

[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
result = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(result)

# Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
result = [[country[0][0].upper(), country[0][0][:3].upper(), country[0][1].upper()] for country in countries]
print(result)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]
dictionaries = [{'country': country[0][0].upper(), 'city': country[0][1].upper()} for country in countries]

print(dictionaries)

#6.Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
result = [' '.join(name[0]) for name in names]

print(result)

#Write a lambda function which can solve a slope or y-intercept of linear functions.
linear_func = lambda x, slope, y_intercept: slope * x + y_intercept
slope = 2
y_intercept = 3
x = 5

result = linear_func(x, slope, y_intercept)
print(result)
