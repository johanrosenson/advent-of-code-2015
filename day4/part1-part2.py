# https://adventofcode.com/2015/day/4
from hashlib import md5

input = open('input').read()

number1 = None
hash1 = None
number2 = None
hash2 = None

for number in range(10000000):
    key = '{}{}'.format(input, number)
    hash = md5(key.encode('utf-8')).hexdigest()

    if number1 == None and hash.startswith('00000'):
        number1 = number
        hash1 = hash

    if number2 == None and hash.startswith('000000'):
        number2 = number
        hash2 = hash

    if number1 != None and number2 != None:
        break

print('Hashes found:')
if number1 == None:
    print('No hash found for number1')
else:
    print('Hash for number1 found with number {} (Hash: {})'.format(number1, hash1))

if number2 == None:
    print('No hash found for number2')
else:
    print('Hash for number2 found with number {} (Hash: {})'.format(number2, hash2))
