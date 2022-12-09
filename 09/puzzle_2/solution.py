#!/usr/bin/env python3

class Rope:
    def __init__(self):
        self.head_x = 0
        self.head_y = 0
        self.tail_x = 0
        self.tail_y = 0
        self.visits = {self.tail}

    @property
    def head(self):
        return (self.head_x, self.head_y)

    @property
    def tail(self):
        return (self.tail_x, self.tail_y)

    def move_head(self, x=0, y=0):
        self.head_x += x
        self.head_y += y

        move = [a - b for a, b in zip(self.head, self.tail)]

        if abs(move[0]) <= 1 and abs(move[1]) <= 1:
            return
        if abs(move[0]) == 2 and abs(move[1]) == 2:
            self.tail_x += move[0] / 2
            self.tail_y += move[1] / 2
        elif abs(move[0]) == 2:
            self.tail_x += move[0] / 2
            self.tail_y = self.head_y
        elif abs(move[1]) == 2:
            self.tail_x = self.head_x
            self.tail_y += move[1] / 2

        self.visits.add(self.tail)

    def change_head(self, direction):
        match direction:
            case "U":
                self.move_head(y=1)
            case "D":
                self.move_head(y=-1)
            case "L":
                self.move_head(x=-1)
            case "R":
                self.move_head(x=1)


def main(filename):
    rope = [Rope() for r in range(9)]
    with open(filename) as f:
        for item in f.read().splitlines():
            direction, moves = item.strip().split(" ")
            for m in range(int(moves)):
                rope[0].change_head(direction)
                for r in range(8):
                    x = rope[r].tail_x
                    y = rope[r].tail_y
                    rope[r+1].move_head(x, y)

    return len(rope[8].visits)


if __name__ == "__main__":
    print(main("input.txt"))
