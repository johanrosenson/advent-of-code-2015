# https://adventofcode.com/2015/day/8

strings = open('input').read().splitlines()
# strings = open('example').read().splitlines()

strlen_encoded = 0
strlen_decoded = 0

for string in strings:
    strlen_encoded += len(string)
    decoded = eval(string)
    strlen_decoded += len(decoded)

strlen_diff = strlen_encoded - strlen_decoded

print('Diff: {}'.format(strlen_diff))
