class Toy():

  def __init__(self, color, age):
    self.color = color
    self.age = age
    self.my_dict = {
      'name': 'Snorlax',
      'is_sleepy': True
    }

  def __str__(
      self
  ):  # we can actually modify the dunder methods to change what it does
    return f'{self.color}'

  def __len__(self):
    return 5

  def __call__(self):
    return 'yesss???????'

  def __getitem__(self, i):
    return self.my_dict[i]

action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))  # str and __str__() are the same
print(len(action_figure))
print(action_figure())
print(action_figure['name'])
