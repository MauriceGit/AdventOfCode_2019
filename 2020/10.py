#!/usr/bin/env python3.7

from utility import *
from functools import lru_cache

@lru_cache
def test(l, prev):

    if len(l) <= 1:
        return 1

    if l[0]-prev > 3:
        return test(l[1:], l[0])

    count = 0
    if l[1]-prev <= 3:
        count += test(l[1:], prev)

    count += test(l[1:], l[0])

    return count


def main():

    lines = sorted(ints(open_data("10.data")))

    diff = defaultdict(int)
    diff[lines[0]] = 1
    diff[3] = 1

    for i in range(1, len(lines)):
        diff[lines[i] - lines[i-1]] += 1

    print(diff[1]*diff[3])

    print(test(tuple(lines), 0))

if __name__ == "__main__":
    main()

# solution for 10.01: 2100
# solution for 10.02: 16198260678656
