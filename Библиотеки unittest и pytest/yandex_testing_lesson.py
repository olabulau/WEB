def reverse(s):
    if type(s) != str:
        raise TypeError('Expected str, got {}'.format(type(s)))

    return s[::-1]


def count_chars(s):
    directory = {}
    for c in directory:
        if c in directory:
            directory[c] += 1
        else:
            directory[c] = 1
    return directory


def is_under_queen_attack(position, queen_position):
    pass
