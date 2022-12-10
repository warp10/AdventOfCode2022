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


class CRT:
    def __init__(self):
        self.pixels = 40
        self.lines = 6
        self.current_line = 0
        self.current_pixel = 0
        self.framebuffer = self.init_framebuffer()

    def init_framebuffer(self):
        return [['.' for p in range(self.pixels)] for p in range(self.lines)]

    def light(self):
        self.framebuffer[self.current_line][self.current_pixel] = '#'

    def draw(self):
        for i in self.framebuffer:
            print(''.join(i))

class Program:
    def __init__(self, filename):
        self.code = self.load_program(filename)
        self.cpu = CPU()
        self.clock = Clock()
        self.crt = CRT()

    def draw_crt(self):
        self.crt.draw()

    def get_sprite_position(self):
        pos = self.cpu.x_register
        return range(pos - 1, pos + 2)

    def light_pixel(self):
        if self.clock.cycle % self.crt.pixels in self.get_sprite_position():
            self.crt.light()

    def move_crt_beam(self):
        self.crt.current_pixel += 1
        if not self.crt.current_pixel % self.crt.pixels:
            self.crt.current_pixel = 0
            self.crt.current_line += 1

    def load_program(self, filename):
        with open(filename) as f:
            return f.read().splitlines()

    def tick_clock(self):
        self.clock.tick()

    def sync_all(self):
        self.light_pixel()
        self.tick_clock()
        self.move_crt_beam()

    def run_program(self):
        for cmd in self.code:
            self.sync_all()
            if cmd == "noop":
                self.cpu.noop()
            if cmd.startswith("addx"):
                self.sync_all()
                self.cpu.addx(int(cmd.split(" ")[1]))


def main(filename):
    program = Program(filename)
    program.run_program()

    return program.draw_crt()


if __name__ == "__main__":
    print(main("input.txt"))
