'''test123123123'''
# list comprehensions
# we can actually use for loops inside of lists and we can set if conditions
my_list = [char for char in 'hello']
my_list2 = [num for num in range(100)]
my_list3 = [num ** 2 for num in range(100)]
my_list4 = [num ** 2 for num in range(100) if num % 2 == 0]
# print(my_list4)

# set comprehensions are the same as list comprehensions but with sets instead
# however, sets are still different from lists as they only allow unique values

# dicitonary comprehensions
my_dict = {num:num*2 for num in [1,2,3]}
print(my_dict)
