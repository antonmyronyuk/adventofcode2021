"""
Number representation:

 0000
1    2
1    2
 3333
4    5
4    5
 6666

So there {2, 5} means digit 1
{0, 2, 5} - digit 7
{1, 3, 2, 5} - digit 4
and so on
"""

INT_SIGNAL_TO_DIGIT_MAP = {
    frozenset({0, 1, 2, 4, 5, 6})       : 0,
    frozenset({2, 5})                   : 1,
    frozenset({0, 2, 3, 4, 6})          : 2,
    frozenset({0, 2, 3, 5, 6})          : 3,
    frozenset({1, 3, 2, 5})             : 4,
    frozenset({0, 1, 3, 5, 6})          : 5,
    frozenset({0, 1, 3, 4, 5, 6})       : 6,
    frozenset({0, 2, 5})                : 7,
    frozenset({0, 1, 2, 3, 4, 5, 6})    : 8,
    frozenset({0, 1, 2, 3, 5, 6})       : 9,
}


def get_signals_by_length(signals, length):
    return [signal for signal in signals if len(signal) == length]


def char_diff(s1, s2):
    if len(s1) < len(s2):
        s1, s2 = s2, s1

    diff = set(s1) - set(s2)
    return diff.pop()


def get_position_to_char_map(signals):
    position_to_char_map = {}

    # unambiguous numbers
    one = get_signals_by_length(signals, 2)[0]
    four = get_signals_by_length(signals, 4)[0]
    seven = get_signals_by_length(signals, 3)[0]
    eight = get_signals_by_length(signals, 7)[0]

    # ambiguous numbers
    zero_six_nine = get_signals_by_length(signals, 6)

    # 7 - 1
    position_to_char_map[0] = char_diff(seven, one)

    # (8 - 0) + (8 - 6) + (8 - 9)
    chars = [char_diff(eight, num) for num in zero_six_nine]
    assert len(chars) == 3

    for char in chars:
        if char not in four:
            position_to_char_map[4] = char
            rest = [c for c in chars if c != char]
            if rest[0] in one:
                position_to_char_map[2] = rest[0]
                position_to_char_map[3] = rest[1]
            else:
                position_to_char_map[2] = rest[1]
                position_to_char_map[3] = rest[0]
            break

    if one[0] == position_to_char_map[2]:
        position_to_char_map[5] = one[1]
    else:
        position_to_char_map[5] = one[0]

    rest = list(set(eight) - set(position_to_char_map.values()))
    if rest[0] in four:
        position_to_char_map[1] = rest[0]
        position_to_char_map[6] = rest[1]
    else:
        position_to_char_map[1] = rest[1]
        position_to_char_map[6] = rest[0]

    assert len(position_to_char_map) == 7
    return position_to_char_map


def get_number(signals, digits):
    position_to_char_map = get_position_to_char_map(signals)
    char_to_position_map = {v: k for k, v in position_to_char_map.items()}

    number = ''
    for digit in digits:
        int_signal = frozenset([char_to_position_map[char] for char in digit])
        number += str(INT_SIGNAL_TO_DIGIT_MAP[int_signal])

    return int(number)


with open('input.txt') as input_file:
    res = 0
    lines = [line for line in input_file.read().split('\n') if line]
    for line in lines:
        signals, digits = [x.split(' ') for x in line.split(' | ')]
        res += get_number(signals, digits)


print(res)
