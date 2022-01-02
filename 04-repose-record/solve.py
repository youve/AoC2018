#!/bin/env python3

import fileinput
from dataclasses import dataclass


@dataclass
class Guard():
    number: str
    sleep_schedule: list
    sleep_total: int = 0


def parse(file):
    '''[1518-06-12 23:57] Guard #2633 begins shift
[1518-04-11 00:09] falls asleep
[1518-04-10 00:56] falls asleep
[1518-10-22 00:36] wakes up'''
    lines = []
    for line in file:
        lines.append(line)
    lines = sorted(lines)

    guards = {}
    guard = ""
    sleep_start = ""
    sleep_end = ""
    for line in lines:
        if "begins" in line:
            guard = line.split()[3]
            if guard not in guards:
                guards[guard] = Guard(guard, [0]*60)
        elif "falls asleep" in line:
            sleep_start = line[15:17]
            if sleep_start.startswith('0'):
                sleep_start = int(sleep_start[-1])
            else:
                sleep_start = int(sleep_start)
        elif "wakes" in line:
            sleep_end = line[15:17]
            if sleep_end.startswith('0'):
                sleep_end = int(sleep_end[-1])
            else:
                sleep_end = int(sleep_end)
            guards[guard].sleep_total += (sleep_end - sleep_start)
            for i in range(sleep_start, sleep_end):
                guards[guard].sleep_schedule[i] += 1
    return guards


def part_1(guards):
    print("Part 1: ")
    sleepy = sorted(guards.keys(), key=lambda x: guards[x].sleep_total)[-1]
    print(f"The sleepiest guard is: {guards[sleepy]}")
    most_slept_minute = max(guards[sleepy].sleep_schedule)
    sleepiest_minute = guards[sleepy].sleep_schedule.index(most_slept_minute)
    print(f"The sleepiest minute is: {sleepiest_minute}")

    print(int(sleepy[1:]) * sleepiest_minute)


def part_2(guards):
    print("\nPart 2: ")
    sleepy = sorted(guards.keys(), key=lambda x: max(
        guards[x].sleep_schedule))[-1]
    sleepiest_guard = guards[sleepy]
    most_slept_minute = max(guards[sleepy].sleep_schedule)
    sleepiest_minute = guards[sleepy].sleep_schedule.index(most_slept_minute)
    print(f"The sleepiest guard is: {guards[sleepy]}")
    print(f"The sleepiest minute is: {sleepiest_minute}")

    print(int(sleepy[1:]) * sleepiest_minute)


guards = parse(fileinput.input())
part_1(guards)
part_2(guards)
