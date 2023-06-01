# Writ a function which generates a six digit/character random_user_id.
import random
import string
def random_user_id():
 characters= string.ascii_letters + string.digits
 user_id=''.join(random.choices(characters,k=6))
 return user_id
print(random_user_id())
#   '1ee33d'

# Modify the previous task. Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
# print(user_id_gen_by_user()) # user input: 5 5
import random
import string

def user_id_gen_by_user():
    length = int(input("Enter the number of characters for the user ID: "))
    count = int(input("Enter the number of user IDs to generate: "))
    user_ids = []
    
    for i in range(count):
        user_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
        user_ids.append(user_id)
    
    return user_ids
user_ids = user_id_gen_by_user()
for user_id in user_ids:
    print(user_id)

# Write a function named rgb_color_gen. 
# It will generate rgb colors (3 values ranging from 0 to 255 each).

def rgb_color_gen():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    
    return f"rgb({red},{green},{blue})"

print(rgb_color_gen())


# Exercises: Level 2
# Write a function list_of_hexa_colors which
#  returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #.
#  Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f.
#  Check the task 6 for output examples).

import random

def list_of_hexa_colors(num_colors):
    colors = []
    
    for _ in range(num_colors):
        color = '#'
        for _ in range(6):
            color += random.choice('0123456789ABCDEF')
        colors.append(color)
    
    return colors

# Generate 5 hexadecimal colors
print(list_of_hexa_colors(5))



# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
# Write a function generate_colors which can generate any number of hexa or rgb colors.

import random

def generate_colors(num_colors, color_type):
    colors = []
    
    if color_type == "hexa":
        for _ in range(num_colors):
            color = '#'
            for _ in range(6):
                color += random.choice('0123456789ABCDEF')
            colors.append(color)
    elif color_type == "rgb":
        for _ in range(num_colors):
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            colors.append(color)
    
    return colors

# Generate 5 hexa colors
print(generate_colors(5, "hexa"))

# Generate 5 RGB colors
print(generate_colors(5, "rgb"))

print(generate_colors(3,'hexa')) # ['#a3e12f','#03ed55','#eb3d2b'] 
print(generate_colors(1,'hexa'))# ['#b334ef']
print(generate_colors(3,'rgb')) # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
print(generate_colors(1,'rgb'))  # ['rgb(33,79, 176)']




# Exercises: Level 3
# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
import random

def shuffle_list(lst):
    random.shuffle(lst)
    return lst

# Example usage
my_list = [1, 2, 3, 4, 5]
shuffled_list = shuffle_list(my_list)
print(shuffled_list)

# Write a function which returns an array of seven random numbers
#  in a range of 0-9. All the numbers must be unique.
import random

def generate_unique_random_numbers():
    numbers = random.sample(range(10), 7)
    return numbers

print(generate_unique_random_numbers())
 


 
