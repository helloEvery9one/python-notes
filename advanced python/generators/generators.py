'''
generators
'''
# generators are things that can generate a sequence of values over time
# for example, range() is a generator because it generates a sequence of numbers
# for i in range(100):  # keep in mind that generators generate values ONE-BY-ONE
# print(i)


# we can make our own generator below:


def generator(num):
    '''generator function'''
    for i in range(num):
        yield i  # pauses the generator function when the range reaches the maximum amount


g = generator(100)
next(g)  # next keyword runs the generator function and gives us
# the next value in the iteration
# we start with 0 first (unless u define 1 as the start) and then continues from there
# next keyword can be used as many times as possible until the range reaches the max
next(g)
next(g)
print(next(g))
