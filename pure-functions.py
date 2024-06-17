from functools import reduce

# pure function - a function that returns the same output when given an input
# there are 2 rules for pure functions:
# 1. it should return the same output every time when given the same input
# 2. it shouldn't have any side effects

# def multiply_by2(li):
#   new_list = []
#   for item in li:
#     new_list.append(item*2)

#   return new_list

# print(multiply_by2([1,2,3]))

#------------------------useful functions----------------------------
# map, filter, zip, reduce
# MAP
my_list = [1, 2, 3]
your_list = [10, 20, 30]


def multiply_by2(item):
  return item * 2


print(list(map(multiply_by2, my_list)))
print(my_list)
# in this example, map runs a function and takes another argument as an iterable
# map() actually creates a whole new list and the outside doesn't get affected


# FILTER
def only_odd(item):
  return item % 2 != 0


print(list(filter(only_odd, my_list)))
# in this example, filter takes the same arguments as map
# filter() filters out any value that is considered False
# in this function, the return statement only returns a value if it is True
# since 2 / 2 has a remainder of 0, filter() removes that value


# ZIP
print(list(zip(my_list, your_list)))
# zip function takes any amount of iterables
# zip takes the first value of EACH iterable and combines them into a tuple
# then, it moves on to the next value and does the same
# it repeats this until everything is zipped together


# REDUCE
# reduce actually needs a module to be imported (you can see at the top)
def accumulator(acc, item):
  print(acc, item)
  return acc + item
  
print(reduce(accumulator, my_list, 0))