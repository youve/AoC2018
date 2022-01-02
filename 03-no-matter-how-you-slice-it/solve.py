#!/bin/env python3

import fileinput
from dataclasses import dataclass


@dataclass
class Claim:
    claim_id: str
    x: int
    y: int
    x_len: int
    y_len: int


def parse(file):
    claims = []
    for line in file:
        line = line.strip()
        if line:
            line = line.split(" ")
            claim_id = line[0]
            x = int(line[2].split(",")[0])
            y = int(line[2].split(",")[1][:-1])
            x_len, y_len = [int(i) for i in line[3].split("x")]
            claims.append(Claim(claim_id, x, y, x_len, y_len))
    return claims


def check_for_overlaps(claims, fabric):
    for claim in claims:
        bad = False
        for x in range(claim.x, claim.x + claim.x_len):
            for y in range(claim.y, claim.y + claim.y_len):
                if fabric[y][x] > 1:
                    bad = True
        if not bad:
            return claim.claim_id


def overlapping_inches(fabric):
    counter = 0
    for x in fabric:
        for y in x:
            if y > 1:
                counter += 1
    return(counter)


def stake_claims(claims):
    fabric = [[0 for x in range(1000)] for y in range(1000)]

    for claim in claims:
        for x in range(claim.x, claim.x + claim.x_len):
            for y in range(claim.y, claim.y + claim.y_len):
                fabric[y][x] += 1
    return fabric


claims = parse(fileinput.input())

fabric = stake_claims(claims)

print(f"Part 1: {overlapping_inches(fabric)}")
print(f"Part 2: {check_for_overlaps(claims, fabric)}")
