#!/usr/bin/env python3

# Starting items: ordered list of worry level for each item
# Operation: how worry level changes upon monkey inspection
# Test: condition to decide who to throw the item to

# Whole process:
# 1) Starting Value
# 2) Operation
# 3) Test
# 4) Execution

# Round:
# 1) each monkey will process all items before passing on to the next monkey
# 2) Thrown objects go the end of the recipient's queue
# 3) If a monkey has no items, it passes on to the next monkey

# Goal:
# 1) Count the total number of inspected item per monkey after 10000 rounds
# 2) Return the product of the two most active monkeys in the list

import re

ITEMS_REGEX = "[0-9]{1,2}"
ROUNDS_NUMBER = 10000

class Monkey:
    def __init__(self, number):
        self.number = number
        self.items = []
        self.operation = ''
        self.test = 0
        self.true_monkey = 0
        self.false_monkey = 0
        self.inspected_items = 0


class KeepAway:
    def __init__(self):
        self.monkeys = []

    def parse_input(self, filename):
        with open(filename) as f:
            lines = list(map(str.strip, f.read().splitlines()))

        monkey_number = -1
        current_monkey = None

        for line in lines:
            if line.startswith("Monkey"):
                monkey_number += 1
                current_monkey = Monkey(monkey_number)
                self.monkeys.append(current_monkey)
            elif line.startswith("Starting items:"):
                items = re.findall(ITEMS_REGEX, line)
                current_monkey.items = list(map(int, items))
            elif line.startswith("Operation:"):
                current_monkey.operation = line.split('=')[-1].strip()
            elif line.startswith("Test:"):
                current_monkey.test = int(line.split(' ')[-1])
            elif line.startswith("If true"):
                current_monkey.true_monkey = int(line.split(' ')[-1])
            elif line.startswith("If false"):
                current_monkey.false_monkey = int(line.split(' ')[-1])

    def calculate_gcd(self):
        # Playing with modulo arithmetic to make it waaaaaay faster.
        # We are not interested in the actual value of the item, just
        # in the number of inspected items. Dividing the item by the
        # Greatest Common Divisor will give us the same result in terms
        # of checking divisibility and keep numbers small enough to be
        # processed quickly
        self.gcd = 1
        for monkey in self.monkeys:
            self.gcd *= monkey.test

    def do_single_round(self):
        for monkey in self.monkeys:
            items = monkey.items.copy()
            for _ in items:
                monkey.inspected_items += 1
                # Calling "old" the item, just to save me from mangling monkey.operation
                old = monkey.items.pop(0)
                old = eval(monkey.operation)
                old %= self.gcd
                if old % monkey.test == 0:
                    self.monkeys[monkey.true_monkey].items.append(old)
                else:
                    self.monkeys[monkey.false_monkey].items.append(old)

    def process_rounds(self, rounds):
        for _ in range(rounds):
            self.do_single_round()

    def most_active_monkeys(self):
        inspections = [monkey.inspected_items for monkey in self. monkeys]
        res = sorted(inspections)[-2:]
        return res[0] * res[1]


def main(filename):
    ka = KeepAway()
    ka.parse_input(filename)
    ka.calculate_gcd()
    ka.process_rounds(ROUNDS_NUMBER)

    return ka.most_active_monkeys()

if __name__ == "__main__":
    print(main("input.txt"))
