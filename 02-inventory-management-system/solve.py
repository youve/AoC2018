#!/bin/env python3

import fileinput
import collections
import itertools


def solve_part_1(file):
    twos = 0
    threes = 0
    for line in file:
        line = collections.Counter(line)
        if 2 in line.values():
            twos += 1
        if 3 in line.values():
            threes += 1
    return twos * threes


def solve_part_2(lines):
    perms = itertools.permutations(lines, 2)

    for perm in perms:
        if distance(*perm) == 1:
            answer = []
            for i, v in enumerate(perm[0]):
                if v == perm[1][i]:
                    answer.append(v)
            return ''.join(answer)


def parse_file(file):
    lines = [line.strip() for line in file]
    return lines


def distance(a, b):
    differences = 0
    for i, v in enumerate(a):
        if v != b[i]:
            differences += 1
    return differences


lines = parse_file(fileinput.input())
print(f"Part 1: {solve_part_1(lines)}")
print(f"Part 2: {solve_part_2(lines)}")
