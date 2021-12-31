def roll_dice(max_value, num_rolls):
    cur = 0
    while True:
        yield sum((cur + k) % max_value + 1 for k in range(num_rolls))
        cur += num_rolls


def calc_looser_score(pos):
    dice_roller = roll_dice(100, 3)
    turns = 0
    scores = [0, 0]
    player = 0
    while True:
        other_player = 1 - player
        pos[player] = (pos[player] - 1 + next(dice_roller)) % 10 + 1
        turns += 3
        scores[player] += pos[player]
        if scores[player] >= 1000:
            return scores[other_player] * turns

        player = other_player


if __name__ == '__main__':
    print(calc_looser_score(pos=[6, 9]))
