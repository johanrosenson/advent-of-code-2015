# https://adventofcode.com/2015/day/1

input = open('input').read()

print('Floor #{}'.format(
    input.count('(') - input.count(')')
))
