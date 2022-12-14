#!/usr/bin/env python3
"""https://adventofcode.com/2022/day/3"""


# Use index + 1 to get the priority
prio = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total_pt1 = 0
total_pt2 = 0
elf_group = []
with open("3.txt", "r") as f:
    for line in f.readlines():
        line = line.rstrip()

        # Part 1
        a = line[0:int(len(line)/2)]
        b = line[int(len(line)/2):]
        # Use set intersection to find the overlapping elements
        intersect = list(set(a) & set(b))
        total_pt1 += list(prio).index(intersect[0]) + 1

        # Part 2
        elf_group.append(set(line))
        # Gather 3 elves at a time before finding the intersection
        if len(elf_group) == 3:
            intersect = list(elf_group[0] & elf_group[1] & elf_group[2])
            total_pt2 += list(prio).index(intersect[0]) + 1
            # Reset for next set of 3
            elf_group = []

print(f"Part 1: {total_pt1}")
print(f"Part 2: {total_pt2}")
