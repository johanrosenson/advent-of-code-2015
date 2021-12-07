input = open('../input.txt').read()

print('Floor #{}'.format(
    input.count('(') - input.count(')')
))
