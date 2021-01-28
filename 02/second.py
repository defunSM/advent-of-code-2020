import os
import random
import sys


def main():
    file1 = open("input.txt", "r")
    lines = file1.readlines()
    pass_rules = []
    letters = []
    passwords = []
    for pass_rule in lines:
        pass_rule = pass_rule.split(" ")
        pass_rules.append(pass_rule[0])
        letters.append(pass_rule[1].split(":")[0])
        passwords.append(pass_rule[2].split("\n")[0])

    maxs = []
    mins = []

    for i in pass_rules:
        maxs.append(int(i.split("-")[1]))
        mins.append(int(i.split("-")[0]))

    valid = 0
    for i in range(0, 1000):
        # print(i
        count = 0
        for char in passwords[i]:
            if letters[i] == char:
                count = count + 1

        if count <= maxs[i] and count >= mins[i]:
            valid = valid + 1

    print(valid)
    print(maxs)
    print(mins)


main()
