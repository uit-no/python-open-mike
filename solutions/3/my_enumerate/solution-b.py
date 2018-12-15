def my_enumerate(list_, start=0):
    n = start
    for l in list_:
        yield n, l
        n += 1
