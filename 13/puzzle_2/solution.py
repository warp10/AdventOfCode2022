#!/usr/bin/env python3

# Integers: left value <= right value
# Lists: left list smaller or equal then right list
# Type mismatch: integer is converted to li

from itertools import zip_longest
from functools import cmp_to_key


def compare(left, right):
    if not left:
        return -1
    if not right:
        return 1

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    elif isinstance(left, list) and isinstance(right, list):
        for l2, r2 in zip_longest(left, right):
            if (result := compare(l2, r2)) != 0:
                return result
        return 0
    else:
        l2 = [left] if isinstance(left, int) else left
        r2 = [right] if isinstance(right, int) else right
        return compare(l2, r2)

def is_packet_valid(left, right):
    return compare(left, right) <= 0

def main(filename):
    def pairwise(iterable):
        a = iter(iterable)
        return zip(a, a)

    lines = []
    with open(filename) as f:
        for item in f.readlines():
            if item != "\n":
                lines.append(eval(item))

    div1, div2 = [[2]], [[6]]
    sorted_packets = sorted([*lines, div1, div2], key=cmp_to_key(compare))
    return (sorted_packets.index(div1) + 1) * (sorted_packets.index(div2) + 1)


if __name__ == "__main__":
    print(main("input.txt"))
