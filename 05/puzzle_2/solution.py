#!/usr/bin/env python3

import re


def create_start_setup(start_setup):
    positions = []
    stacks = {}

    # Create empty stacks and save data positions for later
    for count, i in enumerate(start_setup[0]):
        if i.isdigit():
            stacks[i] = []
            positions.append(count)

    # Actually populate the stacks with data
    for item in start_setup[1:]:
        for count, position in enumerate(positions, 1):
            try:
                value = item[position]
                if value.isalpha():
                    stacks[str(count)].append(value)
            except IndexError:
                pass

    return stacks


def main(filename):
    with open(filename) as f:
        start_setup, instructions = f.read().split("\n\n")
        start_setup = start_setup.split("\n")[::-1]
        instructions = instructions.split("\n")

    stacks = create_start_setup(start_setup)

    for instruction in filter(lambda i: i != "", instructions):
        counts, frm, to = re.findall("[0-9]+", instruction)

        index = len(stacks[frm]) - int(counts)
        crates = stacks[frm][index:]
        del stacks[frm][index:]
        stacks[to].extend(crates)

    return "".join(stack[-1] for stack in stacks.values())


if __name__ == "__main__":
    print(main("input.txt"))
