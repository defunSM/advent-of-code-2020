#!/usr/bin/env python3

def main():
    file1 = open('input.txt', 'r')
    lines = file1.readlines()

    numbers = []

    for line in lines:
        numbers.append(int(line))

    file1.close()

    for num in range(0, len(numbers)):
        for i in range(0, len(numbers)):
            for b in range(0, len(numbers)):
                if(numbers[num]+numbers[i]+numbers[b] == 2020):
                    print(numbers[num], numbers[i], numbers[b])


main()
