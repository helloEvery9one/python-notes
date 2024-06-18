# functions allow to keep our code dry, which means no repeats
def say_hello():
  print('hello')

# say_hello()
# say_hello()
# say_hello()
# say_hello()


#----------------------parameters vs arguments-------------------------
# parameters are like variables for functions
def greeting(name, special):
  print(f'hello, {name}{special}')

# arguments are the actual values for the parameters
# these are positional arguments
# the position of the value matters
# greeting('daniel', '!')
# greeting('phillip', '.')
# greeting('enzo', '...')

#---------------keyword arguments & default parameters-----------------
# keyword arguments tells specifically which variable should have a certain value
# greeting(special='!!!', name='nigel')

# default parameters are the value of the parameter if one is not given
def cool(say='I am a very cool person, as you can see. You are so lame! Shame on you.'):
  print(say)

# cool('Today, I give out a very important announcement. I graduated high school!!!')
# cool()

#-------------------------return keyword---------------------------
# the return keyword actually returns something
# normally, the function would default to None as the output
# functions can be used as a variable when using the return keyword
# def sum(num1, num2):
#   return num1 + num2

# total = sum(1, 2)
# print(sum(3, total))

#---------------------------docstrings-----------------------------
# docstrings are used to tell other devs what a function does
def test(a):
  '''
  Info: this function tests and prints param a
  '''
  print(a)

# ways to help us know what a function does
# help(test)
# print(test.__doc__)

#------------------------*args & **kwargs--------------------------
# *args can accept any number of arguments; as many as you want
# **kwargs can accept keywords as arguments
# *args returns a tuple and **kwargs returns a dictionary
def super_func(*args, **kwargs):
  total = 0
  for items in kwargs.values():
    total += items
  return sum(args) + total

print(super_func(1,2,3,4,5, num1=12, num2=3))

# ORDER FOR SETTING PARAMETERS: regular params, *args, default params, **kwargs