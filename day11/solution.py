import copy
from collections import deque

with open('input.txt') as input_file:
    original_field = []
    lines = [line for line in input_file.read().split('\n') if line]
    for line in lines:
        original_field.append([int(n) for n in line])

N = len(original_field)
M = len(original_field[0])
SHIFTS = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]


def is_out_of_field_point(i, j):
    return i < 0 or i >= N or j < 0 or j >= M


def get_flashes_count(field):
    flashed = set()
    queue = deque()

    for i in range(N):
        for j in range(M):
            queue.append((i, j))

    while queue:
        i, j = queue.popleft()
        if (i, j) in flashed:
            continue

        field[i][j] += 1
        if field[i][j] >= 10:
            field[i][j] = 0
            flashed.add((i, j))
            for shift_i, shift_j in SHIFTS:
                next_i, next_j = i + shift_i, j + shift_j
                if (
                    not is_out_of_field_point(next_i, next_j)
                    and (next_i, next_j) not in flashed
                ):
                    queue.append((next_i, next_j))

    return len(flashed)


def part1():
    field = copy.deepcopy(original_field)
    return sum(get_flashes_count(field) for _ in range(100))


def part2():
    field = copy.deepcopy(original_field)
    day = 1
    while get_flashes_count(field) != N * M:
        day += 1

    return day


print(part1())
print(part2())
