import string

# alphabet = {char: False for char in string.ascii_lowercase and string.digits}
alphabet = set(string.ascii_lowercase)


def is_pangram(sentence):
    return set(sentence.lower()) >= alphabet
