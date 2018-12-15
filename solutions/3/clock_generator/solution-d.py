def clock_gen():
    i = 1
    j = 1
    n = 24
    while True:
        if (i <= 12):
            yield str(i) + ' am'
            i += 1
        elif (i <= 24):
            yield str(j) + ' pm'
            i += 1
            j += 1
        else:
            yield str(1) + ' am'
            i = 1
            j = 1
