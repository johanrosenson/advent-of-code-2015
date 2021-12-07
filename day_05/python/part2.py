from functions import repeated_group, repeated_offset_letter

strings = open('../input.txt').read().splitlines()

nice_strings = 0

for string in strings:
    if repeated_group(string) and repeated_offset_letter(string):
        nice_strings += 1

print('Nice strings: {}'.format(nice_strings))
