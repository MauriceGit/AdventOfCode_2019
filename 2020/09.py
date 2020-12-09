#!/usr/bin/env python3.7

from utility import *

def is_sum(n, buf):
    c = list(combinations(buf, 2))
    l = lmap(sum, c)
    return n in l


def main():

    lines = open_data("09.data")
    lines = ints(lines)

    preamble = 25

    buf = []
    index = preamble
    for i in range(preamble):
        buf.append(lines[i])

    puzzle_1 = 0

    for i in range(preamble, len(lines)):
        if not is_sum(lines[i], buf):
            puzzle_1 = lines[i]
            break
        buf = buf[1:] + [lines[i]]

    print(puzzle_1)

    puzzle_2 = 0
    min_i, max_i = 0, 0
    while True:
        test = lines[min_i:max_i]
        s = sum(test)
        if s == puzzle_1:
            puzzle_2 = min(test) + max(test)
            break
        if s > puzzle_1:
            min_i += 1
        elif s < puzzle_1:
            max_i += 1

    print(puzzle_2)


if __name__ == "__main__":
    main()

# solution for 09.01: ?
# solution for 09.02: ?
