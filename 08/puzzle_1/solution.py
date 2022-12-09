#!/usr/bin/env python3

visible_trees = 0

def is_visible_left(row, position, tree):
    global visible_trees
    if max(row[:position]) < tree:
        visible_trees += 1
        return True

def is_visible_right(row, position, tree):
    global visible_trees
    if max(row[position + 1:]) < tree:
        visible_trees += 1
        return True

def is_visible_up(matrix, row_count, position, tree):
    global visible_trees
    column = [line[position] for line in matrix]
    if max(column[:row_count]) < tree:
        visible_trees += 1
        return True

def is_visible_down(matrix, row_count, position, tree):
    global visible_trees
    column = [line[position] for line in matrix]
    if max(column[row_count + 1:]) < tree:
        visible_trees += 1
        return

def main(filename):
    global visible_trees
    with open(filename) as f:
        matrix = []
        for item in f.read().splitlines():
            matrix.append(list(map(int, list(item))))

        visible_trees += len(matrix[0]) * 2
        visible_trees += (len(matrix) - 2) * 2

        for row_count, row in enumerate(matrix[1:-1], 1):
            for position, tree in enumerate(row[1:-1], 1):
                if is_visible_left(row, position, tree):
                    continue
                elif is_visible_right(row, position, tree):
                    continue
                elif is_visible_up(matrix, row_count, position, tree):
                    continue
                elif is_visible_down(matrix, row_count, position, tree):
                    continue

    return visible_trees


if __name__ == "__main__":
    print(main("input.txt"))
