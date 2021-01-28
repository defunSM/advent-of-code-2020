#!/usr/bin/env python3

import os
import random
import sys


def main():
    file1 = open('input.txt', 'r')
    lines = file1.readlines()
    pass_rules = []
    letters = []
    passwords = []
    for pass_rule in lines:
        pass_rule = pass_rule.split(" ")
        pass_rules.append(pass_rule[0])
        letters.append(pass_rule[1].split(':')[0])
        passwords.append(pass_rule[2].split("\n")[0])

    maxs = []
    mins = []

    for i in pass_rules:
        maxs.append(int(i.split("-")[1]))
        mins.append(int(i.split("-")[0]))

    valid = 0
    for i in range(0, 1000):
        #print(i)
        length_of_pass = len(passwords[i])-1
        p1 = mins[i]-1
        p2 = maxs[i]-1

        if (length_of_pass >= p1 and length_of_pass < p2):
            if (passwords[i][p1] == letters[i]):
                valid += 1
        elif (length_of_pass >= p2):
            if (passwords[i][p1] == letters[i] and passwords[i][p2] != letters[i]):
                valid += 1
            if (passwords[i][p1] != letters[i] and passwords[i][p2] == letters[i]):
                valid += 1


    print(valid)

main()
