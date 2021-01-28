#!/usr/bin/env python3


def main():
    file1 = open("input.txt", "r")
    lines = file1.readlines()

    forest = []
    for line in lines:
        forest.append(line)

    dir_x = 3
    dir_y = 1

    cur_x = 0
    cur_y = 0

    number_of_trees = 0

    for i in range(322):
        cur_x += dir_x
        cur_y += dir_y

        while cur_x > len(forest[cur_y]) - 1:
            forest[cur_y] = forest[cur_y].replace("\n", "") + forest[cur_y].replace(
                "\n", ""
            )

        if forest[cur_y][cur_x] == "#":
            number_of_trees += 1

        # print(cur_y)
        if cur_y == 322:
            print(forest[cur_y])

    print(number_of_trees)


main()
