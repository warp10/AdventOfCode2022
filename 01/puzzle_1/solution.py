#!/usr/bin/env python3


def main(filename):
    higher = 0
    counter = 0

    with open(filename) as f:
        for item in f.readlines():
            try:
                counter += int(item)
            except ValueError:
                higher = max(counter, higher)
                counter = 0

    return higher


if __name__ == "__main__":
    print(main("input.txt"))
