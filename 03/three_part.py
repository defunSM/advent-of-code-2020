#!/usr/bin/env python3

def main(right, down):
    file1 = open('input.txt', 'r')
    lines = file1.readlines()

    forest = []
    for line in lines:
        forest.append(line)

    dir_x = right
    dir_y = down

    cur_x = 0
    cur_y = 0

    number_of_trees = 0

    while (cur_y < 322):
        cur_x += dir_x
        cur_y += dir_y

        if (cur_y != 324):
            while (cur_x > len(forest[cur_y])-2):
                forest[cur_y] = forest[cur_y].replace('\n', '') + forest[cur_y].replace('\n', '')

        #print(cur_y, ", ", cur_x)
        if (cur_y != 324):
            if (forest[cur_y][cur_x] == '#'):
                number_of_trees += 1

        #print(cur_y)
        #if (cur_y == 322):
        #    print(forest[cur_y])

    #print(number_of_trees)
    return number_of_trees




print(main(1, 1))
print(main(3, 1))
print(main(5, 1))
print(main(7, 1))
print(main(1, 2))
