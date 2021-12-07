import re

instructions = open('../input.txt').read().splitlines()

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
            lights[x][y] += 2

def increase(start, end, diff):
    for x in range(start['x'], end['x']+1):
        for y in range(start['y'], end['y']+1):
            lights[x][y] += diff
            if lights[x][y] < 0:
                lights[x][y] = 0

for instruction in instructions:
    match = re.search(r'(.+)\s(\d+,\d+).+?(\d+,\d+)', instruction)
    op = match.group(1)
    start = xy(match.group(2))
    end = xy(match.group(3))

    if op == 'toggle':
        toggle(start, end)
    else:
        increase(start, end, (-1, 1)[op == 'turn on'])

brightness = 0

for x in range(grid_size):
    for y in range(grid_size):
        brightness += lights[x][y]

print('Total brightness: {}'.format(brightness))
