#!/usr/bin/env python3


class Clock:
    def __init__(self):
        self.cycle = 0

    def tick(self):
        self.cycle += 1


class CPU:
    def __init__(self):
        self.x_register = 1

    def noop(self):
        pass

    def addx(self, x):
        self.x_register += x


class Program:
    def __init__(self, filename):
        self.code = self.load_program(filename)
        self.cpu = CPU()
        self.clock = Clock()
        self.signal_strength = 0

    def load_program(self, filename):
        with open(filename) as f:
            return f.read().splitlines()

    def check_signal_strength(self):
        if self.clock.cycle == 20 \
            or self.clock.cycle > 0 and (self.clock.cycle - 20) % 40 == 0:
            self.signal_strength += self.cpu.x_register * self.clock.cycle

    def tick_clock(self, times=1):
        for t in range(times):
            self.clock.tick()
            self.check_signal_strength()

    def run_program(self):
        for cmd in self.code:
            if cmd == "noop":
                self.tick_clock(1)
                self.cpu.noop()
            if cmd.startswith("addx"):
                self.tick_clock(2)
                self.cpu.addx(int(cmd.split(" ")[1]))


def main(filename):
    program = Program(filename)
    program.run_program()

    return program.signal_strength


if __name__ == "__main__":
    print(main("input.txt"))
