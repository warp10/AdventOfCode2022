#!/usr/bin/env python3

from itertools import zip_longest


def main(filename):
    priority_sum = 0

    with open(filename) as f:
        for first, second, third in zip_longest(*[f] * 3):
            commons = set(first).intersection(second).intersection(third)
            for item in filter(lambda c: c != "\n", commons):
                if item.islower():
                    offset = 96
                elif item.isupper():
                    offset = 38

                priority_sum += ord(item) - offset

    return priority_sum


if __name__ == "__main__":
    print(main("input.txt"))
