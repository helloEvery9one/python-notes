# for loops
# for loops only work with iterable objects
# iterable - things that can be iterated over
# iterate - to check every value one by one in a collection of values
# for item in (1,2,3,4,5):
#   print(item)

#-----------------------------range------------------------------------
# range is a special kind of object that is iterable
# it creates a series of numbers starting with one number and stopping at another number
# for items in range(10):
#   print(items)

# for _ in range(2):
#   print(list(range(10)))

#---------------------------enumerate----------------------------------
# enumerate returns the index value and the value of that index next to each other
# for char in enumerate('hello'):
#   print(char)

#--------------------------while loops---------------------------------
# infinite loop unless there's something to stop it
i = 0
while i < 50:
  print(i)
  i += 1
else: # else condition only runs when there is no break keyword
  print('done with all the work')

#-------------------------loop keywords--------------------------------
# break - exits out of a loop
# continue - continues whatever is above the keyword
# pass - does nothing; a placeholder