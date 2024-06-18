# strings are immutable, meaning they cannot be changed
# can use '' or "" to create strings
# use ''' to create long strings
username = 'benjaminawesome123'
password = "therealbenjamin"
long_string = '''
WOW
0 0
---
'''
# print(long_string)

#------------string concatenation (joining strings together)-----------
# can only concatenate strings
first_name = 'David'
last_name = 'Goggins'
full_name = first_name + ' ' + last_name
# print(full_name)

#--------------------------escape sequences----------------------------
# \t - adds a tab
# \n - adds a new line
# \ - whatever comes after this is a string
weather = "It's \"kind of\" sunny"
# print(weather)

#------------------formatted strings (or f-strings)--------------------
# {} - put a variable name and it will fill in as a string
name = 'Mark'
age = '26'

# print(f'Hi {name}. You are {age} years old.')
# ^^ is the same as:
# print('hi ' + name + '. You are ' + age + ' years old')

#-------------------string indexes (string slicing)--------------------
# starts counting from 0
# indexes can be negative which means that it starts counting from the end to the start
# [start:stop:stepover]
indexes = '012345678'
# print(indexes[0:9:2])