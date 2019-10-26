def is_isogram(string):
    only_alpha = ''.join([c for c in string.lower() if c.isalpha()])
    return len(set(only_alpha)) == len(only_alpha)
