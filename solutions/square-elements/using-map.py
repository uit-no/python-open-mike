def square_element(x):
    return x*x


def square_list1(xs):
    result = map(square_element, xs)
    return list(result)


def square_list2(xs):
    result = map(lambda x: x*x, xs)
    return list(result)


mylist = [1.0, 2.0, 3.0, 4.0, 5.0, 200.0, 1/8]

print(square_list1(mylist))
print(square_list2(mylist))
