def clock_generator():
    times = range(25)
    while True:
        for t in times:
            if t == 0:
                yield '12 pm'
            elif t <= 12:
                yield '{0} am'.format(t)
            else:
                yield '{0} pm'.format(t-12)


my_clock = clock_generator()

for _ in range(28):
    print(next(my_clock))
