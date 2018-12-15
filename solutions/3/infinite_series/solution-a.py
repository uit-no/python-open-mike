def next_element():
    l1 = list(range(1, 6))
    l2 = list(range(5, 0, -1))
    ll = l1 + l2

    while True:
        for l in ll:
            yield l


nn = next_element()
for _ in range(30):
    print(next(nn))
