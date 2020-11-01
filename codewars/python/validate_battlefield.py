# # https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python
# def is_ship(i, j, field):
#     temp_ship = 1
#     field[i][j] = 2
#     horizont = False
#     vertical = False
#
#     while i < len(field):
#         i_plus = False
#         if i + 1 <= len(field):
#             i_plus = True
#
#         if i_plus and field[j][i + 1] == 1:
#             field[j][i + 1] = 2
#             temp_ship += 1
#             horizont = True
#         else:
#             break
#
#         i += 1
#
#     while i > 0:
#         i_minus = False
#         if i - 1 >= 0:
#             i_minus = True
#
#         if i_minus and field[j][i - 1] == 1:
#             field[j][i - 1] = 2
#             temp_ship += 1
#             horizont = True
#         else:
#             break
#
#         i -= 1
#
#     while i < len(field):
#         i_plus = False
#         if i + 1 <= len(field):
#             i_plus = True
#
#         if i_plus and field[i + 1][j] == 1:
#             field[i + 1][j] = 2
#             temp_ship += 1
#             if horizont:
#                 return False
#         else:
#             break
#
#         i += 1
#
#     while i > 0:
#         i_minus = False
#         if i - 1 >= 0:
#             i_minus = True
#
#         if i_minus and field[i - 1][j] == 1:
#             field[i - 1][j] = 2
#             temp_ship += 1
#             if horizont:
#                 return False
#         else:
#             break
#
#         i -= 1
#
#     # while j < range(len(field)):
#     #     j_plus = False
#     #     if j + 1 <= len(field):
#     #         j_plus = True
#     #
#     #     if j_plus and field[i][j + 1] == 1:
#     #         field[i + 1][j] = 2
#     #         temp_ship += 1
#     #         if horizont:
#     #             return False
#     #
#     #         vertical = True
#
#
# def validate_battlefield(field):
#     battleship = []  # 1
#     cruisers = []  # 2
#     destroyers = []  # 3
#     submarines = []  # 4
#
#     for i in range(len(field)):
#         for j in range(len(field)):
#             if field[i][j] == 1:
#                 print("Are you find ship? Checked...")
#                 is_ship(i, j, field)
#
#     return True


def validate_battlefield(field):
    n, m = len(field), len(field[0])

    def check_cell(i, j):
        if 0 <= i < n and 0 <= j < m:
            return field[i][j]
        return 0

    def find_cell(i, j):
        if check_cell(i + 1, j + 1) or check_cell(i + 1, j - 1):
            return 10
        if check_cell(i + 1, j) and check_cell(i, j + 1):
            return 10
        field[i][j] = 2
        if check_cell(i + 1, j):
            return (
                find_cell(i + 1, j) + 1
            )
        if check_cell(i, j + 1):
            return find_cell(i, j + 1) + 1
        return 1

    ships = [0, 0, 0, 0, 0]
    for i in range(n):
        for j in range(m):
            if check_cell(i, j) == 1:
                size = find_cell(i, j)
                if size > 4:
                    return False
                else:
                    ships[size] += 1
    if ships[1:] == [4, 3, 2, 1]:
        return True
    else:
        return False


# def validateBattlefield(field):
#     n, m = len(field), len(field[0])
#     def cell(i, j):
#         if i < 0 or j < 0 or i >= n or j >= m: return 0
#         return field[i][j]
#     def find(i, j):
#         if cell(i + 1, j - 1) or cell(i + 1, j + 1): return 10086
#         if cell(i, j + 1) and cell(i + 1, j): return 10086
#         field[i][j] = 2
#         if cell(i, j + 1): return find(i, j + 1) + 1
#         if cell(i + 1, j): return find(i + 1, j) + 1
#         return 1
#     num = [0] * 5
#     for i in xrange(n):
#         for j in xrange(m):
#             if cell(i, j) == 1:
#                 r = find(i, j)
#                 if r > 4: return False
#                 num[r] += 1
#     [tmp, submarines, destroyers, cruisers, battleship] = num
#     return battleship == 1 and cruisers == 2 and destroyers == 3 and submarines == 4

# from scipy.ndimage.measurements import label, find_objects, np
# def validate_battlefield(field):
#     field = np.array(field)
#     return sorted(
#         ship.size if min(ship.shape) == 1 else 0
#         for ship in (field[pos] for pos in find_objects(label(field, np.ones((3,3)))[0]))
#     ) == [1,1,1,1,2,2,2,3,3,4]

battleField = [
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

print(validate_battlefield(battleField))
