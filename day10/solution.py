OPENING_TO_CLOSING = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>',
}
CLOSING_TO_OPENING = {v: k for k, v in OPENING_TO_CLOSING.items()}

with open('input.txt') as input_file:
    lines = [line for line in input_file.read().split('\n') if line]


def is_valid_brackets_sequence(string):
    stack = []
    for char in string:
        if char in OPENING_TO_CLOSING:
            stack.append(char)
        elif char in CLOSING_TO_OPENING:
            if len(stack) > 0 and stack[-1] == CLOSING_TO_OPENING[char]:
                stack.pop()
            else:
                return False, char

    missing_part = [OPENING_TO_CLOSING[char] for char in reversed(stack)]
    return True, missing_part


def part1():
    bracket_points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    score = 0
    for line in lines:
        is_valid, broken_char = is_valid_brackets_sequence(line)
        if not is_valid:
            score += bracket_points[broken_char]

    return score


def part2():
    bracket_points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    scores = []
    for line in lines:
        is_valid, missing_part = is_valid_brackets_sequence(line)
        if not is_valid:
            continue

        score = 0
        for char in missing_part:
            score *= 5
            score += bracket_points[char]

        scores.append(score)

    return sorted(scores)[len(scores) // 2]


print(part1())
print(part2())
