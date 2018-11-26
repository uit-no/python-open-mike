def my_enumerate(iterable):
    return zip(range(len(iterable)), iterable)


l = ['a', 'b', 'c', 'd', 'e']

for i, element in my_enumerate(l):
    print(i, element)
