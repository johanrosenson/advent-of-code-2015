input = open('../input.txt').read()

route = {'0x0': 1}
x = {0: 0, 1: 0}
y = {0: 0, 1: 0}

for pos in range(len(input)):
    dir = input[pos]
    agent = (1, 0)[pos%2 == 0] # santa is even index, robot is uneven index
    if dir in ['^', 'v']:
        y[agent] += (-1, 1)[dir == '^']
    elif dir in ['>', '<']:
        x[agent] += (-1, 1)[dir == '>']

    coord = '{}x{}'.format(x[agent], y[agent])

    if route.get(coord) == None:
        route[coord] = 0

    route[coord] += 1

print('{} houses recieve atleast one gift'.format(len(route)))
