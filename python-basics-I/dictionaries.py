# dictionaries are unordered
# dictionary keys must be immutable and unique
dictionary = {
  'a': 1,
  'b': 2,
  'c': 3
}
# print(dictionary['b'])


#-----------------------dictionary methods-----------------------------
# print(dictionary.get('c', 100)) # you can set a default value if the key doesn't exist

# print('c' in dictionary.keys())
# print(3 in dictionary.values())
# print(dictionary.items())
# print(dictionary.pop('c')) # returns the value of the key that got removed
