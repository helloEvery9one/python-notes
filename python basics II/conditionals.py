is_old = True
is_licenced = True

# if is_old and is_licenced:
#   print('you are old enough to drive and you can drive')
# else:
#   print('you are not of age')

#------------------------truthy and falsy------------------------------
# python actually evaluates values as True or False
# a truthy value is when the value evaluates as True
# a falsy value is when the value evaluates as False
# truthy examples: 'hello', 123
# falsy examples: '' (empty string), 0

#-----------------------ternary operators------------------------------
# condition_if_true if condition else conditon_if_false
is_friend = True
can_message = 'message allowed' if is_friend else 'not allowed to message'

print(can_message)