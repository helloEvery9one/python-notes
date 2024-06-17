# OOP - object-oriented programming
# classes use CamelCase instead of snake_case
class PlayerCharacter():
  membership = True # class object attribute
  # ^^ is accessible to all objects
  def __init__(self, name, age): # self refers to the class
    self.name = name
    self.age = age

  def run(self):
    return 'run'


player1 = PlayerCharacter('Khang', 13)

# print(player1.run())
# print(player1.membership)

#-----------------@classmethod and @staticmethod--------------------
class Something():
  def __init__(self, say):
    self.say = say

  @classmethod # @classmethod doesn't require instantiation
  def say_something(cls, saying):
    return saying

  @staticmethod # @staticmethod is like classmethod but without "cls"
  def greeting(hello='hello!!!'):
    return hello
  
saying = Something('hello')
# print(saying.say)
# print(Something.greeting())
