# scope - what variables to i have access to?
total = 10 # this is a global scope, meaning anything has access to it

def some_func():
  total = 10 # this is a function scope, meaning that only the function can use it
  print(total)

# however, variables in conditions are still global
if True:
  x = 100

# print(x)

#-------------------------scope order------------------------------
# 1. start with local scope
# 2. if there's no local scope, python checks the parent scope
# 3. if there's also no parent scope, python checks the global scope
# 4. if all of the above fails, python checks the built-in functions
# 5. NameError if everything above fails

#------------------------scope keywords-----------------------------
# global keyword - tells python to use the global variable
total = 0
def count():
  global total
  total += 1
  return total

# count()
# count()
# print(count)

# nonlocal keyword - tells python to use parent variable but not global variable
x = 'nonlocal'
def outer():
    x = "local"
    def inner():
        nonlocal x
        print("inner:", x)
    inner()
    print("outer:", x)
  
# outer()

