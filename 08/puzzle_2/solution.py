#!/usr/bin/env python3

def score_left(row, position, tree):
    score = 0
    for item in row[:position][::-1]:
        score += 1
        if item >= tree:
            break
    return score

def score_right(row, position, tree):
    score = 0
    for item in row[position + 1:]:
        score += 1
        if item >= tree:
            break
    return score

def score_up(matrix, row_count, position, tree):
    score = 0
    column = [line[position] for line in matrix]
    for item in column[:row_count][::-1]:
        score += 1
        if item >= tree:
            break
    return score

def score_down(matrix, row_count, position, tree):
    score = 0
    column = [line[position] for line in matrix]
    for item in column[row_count + 1:]:
        score += 1
        if item >= tree:
            break
    return score

def main(filename):
    best_score = 0

    with open(filename) as f:
        matrix = []
        for item in f.read().splitlines():
            matrix.append(list(map(int, list(item))))

        for row_count, row in enumerate(matrix):
            for position, tree in enumerate(row):
                current_score = 1
                current_score *= score_left(row, position, tree)
                current_score *= score_right(row, position, tree)
                current_score *= score_up(matrix, row_count, position, tree)
                current_score *= score_down(matrix, row_count, position, tree)
                if current_score > best_score:
                    best_score = current_score

    return best_score


if __name__ == "__main__":
    print(main("input.txt"))
