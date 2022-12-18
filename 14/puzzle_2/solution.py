#!/usr/bin/env python3


def main(filename):
    with open(filename) as f:
        input = f.read().strip()

    rocks = set()
    for line in input.split("\n"):
        coordinates = [tuple(map(int, p.split(","))) for p in line.split(" -> ")]
        for i in range(len(coordinates)-1):
            c1, c2 = coordinates[i], coordinates[i+1]
            row_range = range(min(c1[0], c2[0]), max(c1[0], c2[0]) + 1)
            col_range = range(min(c1[1], c2[1]), max(c1[1], c2[1]) + 1)
            rocks.update({(row, col) for row in row_range for col in col_range})

    max_col = max((col for _, col in rocks))
    row, col = (500, 0)
    count = 0
    res = 0
    while True:
        if (row, col) in rocks:
            (row, col) = (500, 0)
        if col > max_col and res == 0:
            res = count
        if (row, col + 1) not in rocks and col < max_col + 1:
            col += 1
        elif (row - 1, col + 1) not in rocks and col < max_col + 1:
            row -= 1
            col += 1
        elif (row + 1, col + 1) not in rocks and col < max_col + 1:
            row += 1
            col += 1
        else:
            count += 1
            rocks.add((row, col))
        if (row, col) == (500, 0):
            res = count
            break

    return res

if __name__ == "__main__":
    print(main("input.txt"))
