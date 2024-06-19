'''error handling'''
# error handling
# error handing is a way to work around errors if one ever happens
# we can use the 'try' and 'except' keyword to work around those errors

# age = int(input('what is your age? age: ')) # if we enter anything other than a number,
# we will get an error

# as mentioned at the start, we can use the 'try' and 'except' keywords to work around them
# try:
#     age = int(input('what is your age? age: '))
#     print(f'your age is: {age}')
# except:
#     print('please enter a number!')


# if we want to keep asking the user to enter their age, we use a while loop
# to actually stop the program once the user enters their age, we use an
# else statement to end the loop
# while True:
#     try:
#         age = int(input('what is your age? age: '))
#         print(f'your age is: {age}')
#     except ValueError: # we can handle different types of errors by specifying them
#         print('please enter a number.\n')
#     else:
#         print('thank you!')
#         break


try:
    number = int(input('enter a number: '))
except ValueError as invalid_value: # we can assign the error into a variable that we can use
    print(invalid_value)
else:
    print(f'this is the number you entered: {number}')
finally: # this keyword runs after everything is done, no matter what
    print('woohooo job is finished!!!')
