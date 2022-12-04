#!/usr/bin/env python3


def main(filename):
    priority_sum = 0

    with open(filename) as f:
        for item in f.read().splitlines():
            half_size = len(item) // 2
            first, second = item[:half_size], item[half_size:]

            for item in set(first).intersection(second):
                if item.islower():
                    offset = 96
                elif item.isupper():
                    offset = 38

                priority_sum += ord(item) - offset

    return priority_sum


if __name__ == "__main__":
    print(main("input.txt"))
