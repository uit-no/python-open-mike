class my_enumerate:

    def __init__(self, iterable, counter=0):
        self.iterable = iterable
        self.counter = counter
        self.counter_start = counter
        self.iter_size = len(iterable) + counter

    def __iter__(self):
        return self

    def __next__(self):
        if (self.counter < self.iter_size):
            self.counter = self.counter + 1
            return tuple([self.counter-1,
                          self.iterable[self.counter-1-self.counter_start]])
        else:
            raise StopIteration
