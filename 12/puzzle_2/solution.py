#!/usr/bin/env python3


from time import time


def inverse_bfs(matrix, end):
    path = [end]
    level = {end: 0}

    while path:
        current = path.pop(0)
        for neighbor in get_neighbors(matrix, current):
            if neighbor not in level:
                level[neighbor] = level[current] + 1
                path.append(neighbor)

    return level


def get_neighbors(matrix, node):
    x_min = 0
    y_min = 0
    x_max = len(matrix) - 1
    y_max = len(matrix[0]) - 1
    x, y = node

    node_height = ord(matrix[x][y]) - 2

    neighbors = []

    if (x_min < x) and (node_height < ord(matrix[x - 1][y])):
        neighbors.append((x - 1, y))

    if (x < x_max) and (node_height < ord(matrix[x + 1][y])):
        neighbors.append((x + 1, y))

    if (y_min < y) and (node_height < ord(matrix[x][y - 1])):
        neighbors.append((x, y - 1))

    if (y < y_max) and (node_height < ord(matrix[x][y + 1])):
        neighbors.append((x, y + 1))

    return neighbors


def main(filename):
    start = None
    finish = None
    matrix = []
    starts = []
    with open(filename) as f:
        for x, line in enumerate(f):
            matrix.append([])
            for y, item in enumerate(line.strip()):
                if item == "S":
                    item = "a"
                    start = (x, y)
                    starts.append(start)
                elif item == "E":
                    item = "z"
                    finish = (x, y)
                elif item == 'a':
                    starts.append((x, y))
                matrix[-1].append(item)

    answers = inverse_bfs(matrix, finish)

    totals = [answers.get(point) for point in starts if answers.get(point)]

    print(min(totals))

if __name__ == "__main__":
    print(main("input.txt"))
