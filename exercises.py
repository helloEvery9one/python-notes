# from functools import reduce

# exercise 1: age guesser
# birth_year = input('what year were you born? ')
# age = 2024 - int(birth_year)
# print(f'your age is: {age}.')


# ------------------exercise 2: password checker--------------------
username = 'davidgoggins'
password = 'carryboatsandlogs'
password_len = len(password)
hidden_password = '*' * len(password)

# print(f'{username}, your password {hidden_password} is {password_len} letters long.')


# ------------------exercise 3: logical operators-------------------
is_magician = False
is_expert = True

# if is_magician and is_expert:
#   print('you are a master magician')

# elif is_magician and not is_expert:
#   print('at least you\'re getting there')

# elif not is_magician:
#   print('you need magic powers')

# ----------------------exercise 4: counter-------------------------
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0
# for items in my_list:
#   counter += items
# print(counter)

# ----------------exercise 5: check for duplicates------------------
li = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []
# for items in li:
#   if li.count(items) > 1 and items not in duplicates:
#     duplicates.append(items)
# print(duplicates)

# ----------------------exercise 6: tesla---------------------------


def check_driver_age(age=0):
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")

# checkDriverAge(90)
# print('')
# checkDriverAge(10)
# print('')
# checkDriverAge(18)

# -----------exercise 7: highest even number in a list--------------


def highest_even(my_li):
    evens = []
    for items in my_li:
        if items % 2 == 0:
            evens.append(items)
            evens.sort()
            evens.reverse()
    print(evens[0])

# highest_even([1,2,3,10,4,8,12,11])

# -----------------------exercise 8: cats----------------------------
# class Cat:
#   species = 'mammal'
#   def __init__(self, name, age):
#       self.name = name
#       self.age = age

# cat1 = Cat('cat1', 5)
# cat2 = Cat('Cat2', 7)
# cat3 = Cat('Cat3', 3)

# def oldest_cat(*args):
#     return max(args)

# print(f'Oldest Cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')

# ----------------------exercise 9: pets-----------------------------
# class Pets():
#   animals = []
#   def __init__(self, animals):
#       self.animals = animals

#   def walk(self):
#       for animal in self.animals:
#           print(animal.walk())

# class Cat():
#   is_lazy = True

#   def __init__(self, name, age):
#       self.name = name
#       self.age = age

#   def walk(self):
#       return f'{self.name} is just walking around'

# class Simon(Cat):
#   def sing(self, sounds):
#       return f'{sounds}'

# class Sally(Cat):
#   def sing(self, sounds):
#       return f'{sounds}'

# class William(Cat):
#   def sing(self, sounds):
#     return f'{sounds}'

# grey_cat = Simon('Simon', 5)
# black_cat = Sally('Sally', 7)
# orange_cat = William('William', 3)
# my_cats = [grey_cat, black_cat, orange_cat]

# my_pets = Pets(my_cats)
# my_pets.walk()

# -------------------exercise 10: super list-------------------------


class SuperList(list):
    '''hallo hallo hallo'''

    def __len__(self):
        return 1000

# superlist = SuperList()
# print(len(superlist))
# superlist.append(5)
# print(superlist[0])


# ---------------exercise 11: map, filter, zip, reduce---------------
# 1 Capitalize all of the pet names and print the list
# my_pets = ['sisi', 'bibi', 'titi', 'carla']


# def capitalize():
    # lis = []
#     for items in my_pets:
#         li.append(items.capitalize())

#     return li


# print(capitalize())


# # 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5, 4, 3, 2, 1]
# my_numbers.sort()
# print(list(zip(my_strings, my_numbers)))

# # 3 Filter the scores that pass over 50%
# scores = [73, 20, 65, 19, 76, 100, 88]


# def filter_scores(scores):
#     return scores < 50


# print(list(filter(filter_scores, scores)))


# # 4 Combine all of numbers that are in a list on this file using reduce (my_numbers and scores)
# def accumulator(acc, item):
#     return acc + item


# print(reduce(accumulator, (my_numbers + scores)))

# -----------------------------exercise 12: lambda expressions----------------------------------
my_list = [5, 4, 3]
print(list(map(lambda item: item ** 2, my_list)))

a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)

#------------------------------exercise 13: comprehensions--------------------------------------
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = list({items for items in some_list if some_list.count(items) > 1})
print(duplicates)
