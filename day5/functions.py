import re

def three_vowels(string):
	return (False, True)[len(re.findall('[aeiou]', string)) >= 3]

def repeated_letter(string):
	return re.search(r'(.)\1', string) != None

def repeated_group(string):
	return re.search(r'(..).*\1', string) != None

def contains_prohibited(string):
	return re.search(r'ab|cd|pq|xy', string) != None

def repeated_offset_letter(string):
	return re.search(r'(.).\1', string) != None