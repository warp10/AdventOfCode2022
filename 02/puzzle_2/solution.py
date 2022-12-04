#!/usr/bin/env python3

# A, X: Rock
# B, Y: Paper
# C, Z: Scissors

# X: Lose
# Y: Draw
# Z: Win

result_mapping = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

score_mapping = {
    'A': 1,
    'B': 2,
    'C': 3,
}

win_options = {
    'A': 'B',
    'B': 'C',
    'C': 'A',
}

lose_options = {
    'A': 'C',
    'B': 'A',
    'C': 'B',
}


def main(filename):
    score = 0

    with open(filename) as f:
        for item in f.readlines():
            elf, me = item.split()

            if me == 'Y':
                score += score_mapping[elf]
            elif me == 'X':
                score += score_mapping[lose_options[elf]]
            elif me == 'Z':
                score += score_mapping[win_options[elf]]
            score += result_mapping[me]


    return score

if __name__ == "__main__":
    print(main("input.txt"))
