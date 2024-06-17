# sets are an unordered collection of unique objects
# therefore, they only return unique values, so no duplicates
# also, you cannot access sets by using indexes
# to access sets, check for values by using the 'in' keyword
my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9}
# print(my_set)


#---------------------------set methods--------------------------------
# print(my_set.difference(your_set))

# my_set.discard(5)
# print(my_set)

# my_set.difference_update(your_set)
# print(my_set)

# print(my_set.intersection(your_set))
# print(my_set & your_set) # same as intersection but shorter
# print(my_set.isdisjoint(my_set))
# print(my_set.union(your_set))
# print(my_set | your_set) # same as union but shorter
# print(my_set.issubset(your_set))
# print(my_set.issuperset(your_set))