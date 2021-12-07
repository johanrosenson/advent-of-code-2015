input = open('../input.txt').read()

route = {
    '0x0': 1
}

x = 0
y = 0

for dir in input:
    if dir == '^':
        y += 1
    elif dir == 'v':
        y += -1
    elif dir == '>':
        x += 1
    elif dir == '<':
        x += -1

    coord = '{}x{}'.format(x, y)

    if route.get(coord) == None:
        route[coord] = 0

    route[coord] += 1

print('{} houses recieve atleast one gift'.format(len(route)))
