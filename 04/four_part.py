#!/usr/bin/env python3


# AOC Passport processing

def main():
    file1 = open('input.txt', 'r')
    lines = file1.readlines()

    valid = 0

    valid_passports = []
    passports = []
    passport = []

    for i in lines:
        if (i != '\n'):
            passport.append(i.split("\n")[0] + " ")
        else:
            passports.append(''.join(passport))
            passport = []

    for i in passports:
        if ('byr' in i and 'iyr' in i and 'eyr' in i and 'hgt' in i and 'hcl' in i and 'ecl' in i and 'pid' in i):
            valid_passports.append(i[:-1])

    for i in valid_passports:
        keys = i.split(" ")
        for key in keys:
            if ('byr' in key):
                try:
                    digit = int(key.split(":"))
                    if (int(digit) >= 1920 or int(digit) <= 2002):
                        pass
                    else:
                        valid_passports.remove(i)

                except:
                    valid_passports.remove(i)

            if ('iyr' in key):
                try:
                    digit = int(key.split(":")[1])
                    if (int(digit) >= 2010 or int(digit) <= 2002):
                        pass
                    else:
                        valid_passports.remove(i)
                except:
                    valid_passports.remove(i)

            if ('eyr' in key):
                try:
                    digit = int(key.split(":")[1])
                except:
                    valid_passports.remove(i)
                if (int(digit) >= 2020 or int(digit) <= 2030):
                    #valid += 1
                    pass
                else:
                    valid_passports.remove(i)

            if ('hgt' in key):
                value = key.split(":")[1]
                if ('cm' in value):
                    value = int(value.split("cm")[0])
                    if (value >= 150 or value <=193):
                        pass
                    else:
                        valid_passports.remove(i)
                elif ('in' in value):
                    value = int(value.split("in")[0])
                    if (value >= 59 or value <= 76):
                        pass
                    else:
                        break
                else:
                    break

            if ('ecl' in key):
                eye = key.split(":")[1]
                if ( 'amb' == eye or 'blu' == eye or 'brn' == eye or 'gry' == eye or 'grn' == eye or 'hzl' == eye or 'oth' == eye):
                    #valid += 1
                    pass
                else:
                    try:
                        valid_passports.remove(i)
                    except:
                        pass

            if ('hcl:#' in key):
                pass

            if ('pid' in key):
                value = key.split(":")[1]
                if (len(value) == 9):
                    pass
                    valid += 1
                else:
                    valid_passports.remove(i)

            
    
    print("# of passports: %d" % len(passports))
    print("Number of valid passports: ", len(valid_passports))

    print(valid_passports)

main()
