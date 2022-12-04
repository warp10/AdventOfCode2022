#!/usr/bin/env python3

# A, X: Rock
# B, Y: Paper
# C, Z: Scissors

mapping = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}

score_mapping = {
    'A': 1,
    'B': 2,
    'C': 3,
}

win_options = [
    ('A', 'B'),
    ('B', 'C'),
    ('C', 'A'),
]


def main(filename):
    score = 0

    with open(filename) as f:
        for item in f.readlines():
            elf, me = item.split()
            elf, me = elf, mapping[me]

            if elf == me:
                score += 3
            elif (elf, me) in win_options:
                score += 6

            score += score_mapping[me]

    return score

if __name__ == "__main__":
    print(main("input.txt"))
