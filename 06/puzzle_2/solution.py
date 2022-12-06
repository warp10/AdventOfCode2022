#!/usr/bin/env python3


def main(filename):
    with open(filename) as f:
        data = f.read()

        sliding_window_size = 14
        sliding_window_start = 0
        sliding_window_end = sliding_window_size

        while True:
            if (
                len(set(data[sliding_window_start:sliding_window_end]))
                == sliding_window_size
            ):
                return sliding_window_end
            sliding_window_start += 1
            sliding_window_end += 1


if __name__ == "__main__":
    print(main("input.txt"))
