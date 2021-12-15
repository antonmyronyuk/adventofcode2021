from collections import defaultdict

with open('input.txt') as input_file:
    lines = [line for line in input_file.read().split('\n') if line]
    template = lines[0]
    rules = [line.split(' -> ') for line in lines[1:]]
    rules_map = {pair: produced_char for pair, produced_char in rules}


def get_score(days):
    pair_counts = {pair: 0 for pair in rules_map}
    for char1, char2 in zip(template, template[1:]):
        pair = char1 + char2
        pair_counts[pair] += 1

    for _ in range(days):
        next_counts = pair_counts.copy()
        for pair, count in pair_counts.items():
            if count == 0:
                continue

            produced_char = rules_map[pair]
            new_pair1 = pair[0] + produced_char
            new_pair2 = produced_char + pair[1]
            next_counts[new_pair1] += count
            next_counts[new_pair2] += count
            next_counts[pair] -= count

        pair_counts = next_counts

    # each char in result string is counted twice (instead of first and last)
    char_counts = defaultdict(lambda: 0)
    for pair, count in pair_counts.items():
        char_counts[pair[0]] += count
        char_counts[pair[1]] += count

    # count first and last chars also twice
    char_counts[template[0]] += 1
    char_counts[template[-1]] += 1

    return (max(char_counts.values()) - min(char_counts.values())) // 2


if __name__ == '__main__':
    print(get_score(10))  # part 1
    print(get_score(40))  # part 2
