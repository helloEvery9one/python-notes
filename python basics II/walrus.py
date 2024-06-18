# walrus operator - :=
a = 'helllllllloooooooooo'
if (n := len(a)) > 10:
  print(f'variable a is too long. {n} elements, expected less than 10.')

while (n := len(a)) > 1:
  a = a[:-1]
  print(n)