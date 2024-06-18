# lists are data structures and are mutable, meaning that they can be changed
# data structures store information
li = [1,2,3,4,5]
li = ['a', 'b', 'c']
li3 = [1,2,'a',True]

# list slicing
# print(li[0:2])

# matrix - lists inside a list
matrix = [
  [1,2,3],
  [2,4,6],
  [3,6,9]
]


#---------------------------list methods-------------------------------
# some methods changes the list in-place and some do not
# adding:
basket = [1,2,3,4,5]
# basket.append(100) # append changes the list in place and doesn't create a new value
# basket.insert(4, 100) # same rule applies to insert
# basket.extend([100, 101]) 

# removing:
# basket.pop()
# basket.remove(4)
# basket.clear()
# print(basket)

#------------------------list methods part 2---------------------------
basket2 = ['a','b','c','d','e','d']
# print(basket2.index('a')) # returns the index number of a value given

# print(basket2.count('d')) # returns the number of occurrences of a value in a list

# basket2.sort()
# print(basket2)

# basket2.reverse()
# print(basket2)

# list unpacking
a,b,c, *other = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)