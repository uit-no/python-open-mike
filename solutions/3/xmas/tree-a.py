import random


def make_tree(floors=3, decoration='ø0*Å¤@ '):
    '''
    Returns a string depicting a tree with given number of levels/floors.
    Decoration may be given as a string of characters suitable as decoration.
    If no decoration is desired, pass an empty string.
    '''

    if not decoration:
        decoration = ' '
    if floors < 1:
        floors = 1
    elif floors > 10:
        floors = 10

    tree = []

    for floor in range(floors):
        # Add the three rows with diagonals:
        tree.append('{:>4}{}{:<4}'.format('/', ' ' * (floor * 2), '\\'))
        tree.append('{:>3}{}{:<3}'.format('/', ' ' * (floor * 2 + 2), '\\'))
        tree.append('{:>2}{}{:<2}'.format('/', ' ' * (floor * 2 + 4), '\\'))

        # Add the bottom row of the floor:
        row = '{}--{}--{}'.format(
            random.choice(decoration), ' ' * ((floor + 1) * 2),
            random.choice(decoration))
        tree.append(row)

    # For the trunk, the last line has to be changed to close the gap
    tree[-1] = '{}{}+  +{}{}'.format(
        random.choice(decoration), '-' * floors, '-' * floors,
        random.choice(decoration))
    tree.append('+--+')

    # Center all lines
    total_width = floors * 2 + 6
    tree = (row.center(total_width) for row in tree)

    return '\n'.join(tree)


tree = make_tree(5)
print(tree)
