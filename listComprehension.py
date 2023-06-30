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
              