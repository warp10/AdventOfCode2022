#!/usr/bin/env python3

from heapq import nlargest


def main(filename):
    higher = [0, 0, 0]
    counter = 0

    with open(filename) as f:
        for item in f.readlines():
            try:
                counter += int(item)
            except ValueError:
                higher = nlargest(3, [counter, *higher])
                counter = 0

    return sum(higher)

if __name__ == '__main__':
    print(main('input.txt'))
