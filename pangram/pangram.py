import re

ALPHABET = r'[a-z]'
LENGTH_OF_ALPHABET = 26

def is_pangram(sentence):
    return len(set(re.findall(ALPHABET, sentence.lower()))) == LENGTH_OF_ALPHABET
