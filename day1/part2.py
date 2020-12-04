# https://adventofcode.com/2015/day/1

input = open('input').read()

floor = 0

for i in range(len(input)):
    if input[i] == '(':
        floor += 1
    else:
        floor -= 1

    if floor < 0:
        print('Entered the basement on position #{}'.format(i+1))
        break
