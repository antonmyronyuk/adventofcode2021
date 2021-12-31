cache = {}
val_to_freq_map = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


def count_wins(pos, scores, player):
    if scores[0] >= 21:
        return [1, 0]
    if scores[1] >= 21:
        return [0, 1]

    cache_key = (*pos, *scores, player)
    if cache_key in cache:
        return cache[cache_key]

    total_counts = [0, 0]
    for val, freq in val_to_freq_map.items():
        next_pos = pos.copy()
        next_scores = scores.copy()
        next_pos[player] = (next_pos[player] - 1 + val) % 10 + 1
        next_scores[player] += next_pos[player]

        counts = count_wins(next_pos, next_scores, 1 - player)
        total_counts[0] += freq * counts[0]
        total_counts[1] += freq * counts[1]

    cache[cache_key] = total_counts
    return total_counts


if __name__ == '__main__':
    print(max(count_wins(pos=[6, 9], scores=[0, 0], player=0)))
