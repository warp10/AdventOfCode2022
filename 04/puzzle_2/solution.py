#!/usr/bin/env python3


def main(filename):
    overlaps = 0

    with open(filename) as f:
        for item in f.read().splitlines():
            first, second = item.split(",")
            r1_1, r1_2 = first.split("-")
            r2_1, r2_2 = second.split("-")
            r1 = range(int(r1_1), int(r1_2) + 1)
            r2 = range(int(r2_1), int(r2_2) + 1)

            if set(r1).intersection(r2):
                overlaps += 1

    return overlaps


if __name__ == "__main__":
    print(main("input.txt"))
