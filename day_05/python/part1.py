from functions import three_vowels, repeated_letter, contains_prohibited

strings = open('../input.txt').read().splitlines()

nice_strings = 0

for string in strings:
    if three_vowels(string) and repeated_letter(string) and not contains_prohibited(string):
        nice_strings += 1

print('Nice strings: {}'.format(nice_strings))
