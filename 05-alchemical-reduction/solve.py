#!/bin/env python3

import fileinput


def parse(file):
    for line in file:
        # only one line
        polymer = line.strip()
    return polymer


def solve_part1(polymer):
    length = ""
    pairs = ['aA', 'bB', 'cC', 'dD', 'eE', 'fF', 'gG', 'hH', 'iI', 'jJ', 'kK', 'lL',
             'mM', 'nN', 'oO', 'pP', 'qQ', 'rR', 'sS', 'tT', 'uU', 'vV', 'wW', 'xX', 'yY', 'zZ']
    while length != len(polymer):
        length = len(polymer)
        for pair in pairs:
            polymer = polymer.replace(pair, '')
            polymer = polymer.replace(pair[::-1], '')
    return length


def solve_part2(polymer):
    best = len(polymer)
    letters = "abcdefghijklmnopqrstuvwxyz"
    for letter in letters:
        new_polymer = polymer.replace(letter, '')
        new_polymer = new_polymer.replace(letter.upper(), '')
        result = solve_part1(new_polymer)
        best = min(best, result)
    return best


polymer = parse(fileinput.input())
print(f"Part 1: {solve_part1(polymer)}")
print(f"Part 2: {solve_part2(polymer)}")
