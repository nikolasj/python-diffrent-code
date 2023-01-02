first_rectangle = "6 6 8 8"

second_rectangle = "1 8 4 9"
first_rectangle = first_rectangle.split()
second_rectangle = second_rectangle.split()

first_point_x = min(int(first_rectangle[0]), int(second_rectangle[0]), int(first_rectangle[2]),
                    int(second_rectangle[2]))
second_point_x = max(int(first_rectangle[0]), int(second_rectangle[0]), int(first_rectangle[2]),
                     int(second_rectangle[2]))

first_point_y = min(int(first_rectangle[1]), int(second_rectangle[1]), int(first_rectangle[3]),
                    int(second_rectangle[3]))
second_point_y = max(int(first_rectangle[1]), int(second_rectangle[1]), int(first_rectangle[3]),
                     int(second_rectangle[3]))

if (second_point_x - first_point_x) > (second_point_y - first_point_y):
    print((second_point_x - first_point_x) ** 2)
else:
    print((second_point_y - first_point_y) ** 2)




first_point_x = min(int(first_rectangle[0]), int(second_rectangle[0]), int(first_rectangle[2]),
                    int(second_rectangle[2]))
second_point_x = max(int(first_rectangle[0]), int(second_rectangle[0]), int(first_rectangle[2]),
                     int(second_rectangle[2]))

first_point_y = min(int(first_rectangle[1]), int(second_rectangle[1]), int(first_rectangle[3]),
                    int(second_rectangle[3]))
second_point_y = max(int(first_rectangle[1]), int(second_rectangle[1]), int(first_rectangle[3]),
                     int(second_rectangle[3]))

if (second_point_x - first_point_x) > (second_point_y - first_point_y):
    print((second_point_x - first_point_x) ** 2)
else:
    print((second_point_y - first_point_y) ** 2)