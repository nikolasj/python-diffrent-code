# https://www.codewars.com/kata/57675f3dedc6f728ee000256/train/python

# def tower_builder(n_floors, block_size):
#     w, h = block_size


def tower_builder(n_floors, block_size):
    w, h = block_size
    filled_block = '*' * w
    empty_block = ' ' * w
    tower = []
    for n in range(1, n_floors + 1):
        for _ in range(h):
            tower.append(empty_block * (n_floors - n) + filled_block * (2 * n - 1) + empty_block * (n_floors - n))
    return tower


print(tower_builder(1, (1, 1)))
print(tower_builder(3, (4, 2)))
