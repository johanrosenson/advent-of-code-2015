import re

strings = open('../input.txt').read().splitlines()

strlen_original = 0
strlen_encoded = 0

for string in strings:
    strlen_original += len(string)
    # encoded = eval(string)
    encoded = '"' + re.sub(
        r'(["\\])',
        r'\\\1',
        string
    ) + '"'
    strlen_encoded += len(encoded)

strlen_diff = strlen_encoded - strlen_original

print('Diff: {}'.format(strlen_diff))
