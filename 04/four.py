#!/usr/bin/env python3


# AOC Passport processing


def main():
    file1 = open("input.txt", "r")

    lines = file1.readlines()

    valid = 0

    passports = []
    passport = []

    for i in lines:
        if i != "\n":
            passport.append(i.split("\n")[0])
        else:
            passports.append("".join(passport))
            passport = []

    for i in passports:
        if (
            "byr" in i
            and "iyr" in i
            and "eyr" in i
            and "hgt" in i
            and "hcl" in i
            and "ecl" in i
            and "pid" in i
        ):
            valid += 1

    print("# of passports: %d" % len(passports))
    print("Number of valid passports: ", valid + 1)


main()
