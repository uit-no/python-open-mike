# Pure list version (for an easy(er) start):


def my_list_enumerate(mylist, start=0):
    '''
    Pure finite list version. Does not work with iterables and returns a list.
    Should work (at least) with lists, tuples, dicts, and sets.
    '''

    result = []
    for i in range(len(mylist)):
        current_position = i + start
        result.append((current_position, mylist[i]))

    return result


def my_list_comp_enumerate(mylist, start=0):
    '''
    Same as `my_list_enumerate` but using list comprehension.
    '''

    return [(i + start, mylist[i]) for i in range(len(mylist))]


def my_enumerate(iterable, start=0):
    '''
    This function should work with every iterable and is itself a generator.
    '''

    for elem in iterable:
        yield (start, elem)
        start += 1


mylist = ['first element', 'and the second', 'finally, the third']

print(my_list_enumerate(mylist))
print(my_list_comp_enumerate(mylist))
print(my_enumerate(mylist))

for num, elem in my_enumerate(mylist):
    print(num, elem)

print()

for num, elem in my_enumerate(mylist, start=1):
    print(num, elem)
