def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    return (blue_start - blue_pulled) / ((red_start - red_pulled) + (blue_start - blue_pulled))


print(guess_blue(5, 5, 2, 3))
