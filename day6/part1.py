# https://adventofcode.com/2015/day/6
import re

instructions = open('input').read().splitlines()

grid_size = 1000

lights = []

for x in range(grid_size):
    lights.append([])
    for y in range(grid_size):
        lights[x].append(0)

def xy(xy):
    [x, y] = [int(v) for v in xy.split(',')]
    return {'x': x, 'y': y}

def toggle(start, end):
    for x in range(start['x'], end['x']+1):
        for y in range(start['y'], end['y']+1):
            lights[x][y] = (0, 1)[lights[x][y] == 0]

def state(start, end, state):
    for x in range(start['x'], end['x']+1):
        for y in range(start['y'], end['y']+1):
            lights[x][y] = state

for instruction in instructions:
    match = re.search(r'(.+)\s(\d+,\d+).+?(\d+,\d+)', instruction)
    op = match.group(1)
    start = xy(match.group(2))
    end = xy(match.group(3))

    if op == 'toggle':
        toggle(start, end)
    else:
        state(start, end, (0, 1)[op == 'turn on'])

turned_on = 0

for x in range(grid_size):
    for y in range(grid_size):
        if lights[x][y] == 1:
            turned_on += 1

print('Turned on: {}'.format(turned_on))
