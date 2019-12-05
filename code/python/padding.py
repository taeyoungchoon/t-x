#!/usr/bin/env python3

data = [i for i in range(7)]
divider = 3
left = len(data) % divider
padding = divider - left

if left != 0:
    for i in range(padding):
        data.append(None)

galaxy = []
universe = []

for i in data:
    galaxy.append(i)
    if len(galaxy) == divider:
        universe.append(galaxy.copy())
        galaxy.clear()

if left != 0:
    for i in range(padding):
        universe[-1].remove(None)

print(universe)
