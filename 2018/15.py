#!/usr/bin/env python3.7

import sys
sys.path.append('../General')
from utility import *


def bfs(field, units, current_pos, team):

    reading_order = [(0,-1), (-1,0), (1, 0), (0, 1)]
    backtrack = {current_pos: -1}
    visited = set([u[0] for u in units if u[2] == team])
    candidates = [current_pos]
    enemies = {u[0] for u in units if u[2] != team}
    target = None

    while len(candidates) > 0:
        c = candidates.pop(0)
        if c in enemies:
            target = c
            break

        for r in reading_order:
            new_pos = add(c,r)
            if new_pos in visited or new_pos not in field:
                continue

            candidates.append(new_pos)
            backtrack[new_pos] = c
            visited.add(new_pos)

    if target == None:
        return None

    path = []
    p = backtrack[target]
    while backtrack[p] != -1:
        path.append(p)
        p = backtrack[p]

    return path[-1] if len(path) > 0 else None


def length2(p):
    return abs(p[0]) + abs(p[1])


def get_inrange_target(p, units, team):
    t_index = -1
    for i, u in enumerate(units):
        if u[2] != team and length2(sub(u[0], p)) == 1 and (t_index == -1 or u[1] < units[t_index][1]):
            t_index = i
    return t_index


def run_round(field, units):

    i = 0
    while i < len(units):
        u = units[i]

        if all(x[2] == units[0][2] for x in units):
            return False

        next_step = bfs(field, units, units[i][0], units[i][2])
        if next_step != None:
            units[i][0] = next_step

        target_index = get_inrange_target(units[i][0], units, u[2])
        if target_index != -1:
            units[target_index][1] -= 3
            if units[target_index][1] <= 0:
                del units[target_index]
                if target_index < i:
                    continue
        i += 1

    return True


def run(lines):
    units = []
    field = dict()

    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if c != "#":
                field[(x,y)] = 1
                if c in "GE":
                    units.append([(x,y), 200, c == "E"])

    rounds = 0
    while True:
        units.sort(key=lambda x: (x[0][1], x[0][0]))
        if not run_round(field, units):
            break
        rounds += 1

    print((rounds) * sum(x[1] for x in units))


def main():

    groups = open_data_groups("15.data")

    for g in groups:
        run(g)
        print()




if __name__ == "__main__":
    main()

# year 2018
# solution for 15.01: 257954
# solution for 15.02: ?
