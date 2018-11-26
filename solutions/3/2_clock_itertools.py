from itertools import cycle


def clock_generator():
    m = cycle(['am', 'pm'])
    _m = next(m)
    t = cycle([12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    while True:
        _t = next(t)
        yield f'{_t} {_m}'
        if _t == 11:
            _m = next(m)


my_clock = clock_generator()

for _ in range(28):
    print(next(my_clock))
