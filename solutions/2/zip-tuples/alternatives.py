def solution1(xs, ys):
    assert len(xs) == len(ys), "Error: Both lists must have the same lengths!"
    zs = []
    for i, x in enumerate(xs):
        zs.append((x, ys[i]))
    return zs


def solution2(xs, ys):
    assert len(xs) == len(ys), "Error: Both lists must have the same lengths!"
    zs = [(xs[i], ys[i]) for i in range(len(xs))]
    return zs


def solution3(xs, ys):
    zs = list(zip(xs, ys))
    return zs


list1 = ["this", "is", "a", "list"]
list2 = [1, 2, 3, 4]

print(solution1(list1, list2))
print(solution2(list1, list2))
print(solution3(list1, list2))
