def clock_generator():
    '''
    Infinite generator that loops through the hours of the day yielding American-style hours.
    '''

    time = 12
    am = True

    post_string = ('pm', 'am')

    while True:
        # The following yield contains a special formating command:
        # >2 formats the given variable right-aligned with a width of two characters
        # Furthermore, there is a "dirty hack":
        # post_string[am] uses the trick that True is evaluated to 1 and False is evaluated to 0
        # Alternatively, something like the following could be used:
        # if am:
        #     string = 'am'
        # else:
        #     string = 'pm'
        yield '{:>2} {}'.format(time, post_string[am])

        time += 1

        if time == 12:
            am = not am
        elif time == 13:
            time = 1


my_clock = clock_generator()

for _ in range(28):
    print(next(my_clock))
