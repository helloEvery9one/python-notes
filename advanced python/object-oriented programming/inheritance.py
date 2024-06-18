class User():
  
  def sign_in(self):
    return 'logged in'


class Wizard(User):

  def __init__(self, name, power):
    self.name = name
    self.power = power
    # super().__init__(email) # super() allows us to use the superclass (User) without
    # needing to input pass in self parameter

  def attack(self):
    return f'attacking with a power of: {self.power}'


class Archer(User):

  def __init__(self, name, num_arrows):
    self.name = name
    self.num_arrows = num_arrows

  def check_arrows(self):
    return f'arrows left: {self.num_arrows}'


class HybridBorg(Wizard, Archer): # we have to separately call the __init__ for
  # Wizar and Archer if we want to do multipe inheritance
  def __init__(self, name, power, arrows):
    Archer.__init__(self, name, arrows)
    Wizard.__init__(self, name, power)


wizard1 = Wizard('Heredus', 1000)
archer1 = Archer('Usopp', 50000)
hybridborg1 = HybridBorg('Zeus', 50, 100)
print(hybridborg1.check_arrows())
print(hybridborg1.attack())
print(hybridborg1.sign_in())
