from collections import deque

with open('input.txt') as input_file:
    field = []
    lines = [line for line in input_file.read().split('\n') if line]
    for line in lines:
        field.append([int(n) for n in line])

N = len(field)
M = len(field[0])
SHIFTS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def is_out_of_field_point(i, j):
    return i < 0 or i >= N or j < 0 or j >= M


def is_lower_point(i, j, next_i, next_j):
    return (
        is_out_of_field_point(next_i, next_j)
        or field[i][j] < field[next_i][next_j]
    )


def get_minimal_points():
    points = []
    for i in range(N):
        for j in range(M):
            if all(
                is_lower_point(i, j, i + shift_i, j + shift_j)
                for shift_i, shift_j in SHIFTS
            ):
                points.append((i, j))

    return points


def get_basin_size(start_i, start_j):
    size = 0
    queue = deque()
    visited = set()
    queue.append((start_i, start_j))
    visited.add((start_i, start_j))

    while queue:
        size += 1
        i, j = queue.pop()
        for shift_i, shift_j in SHIFTS:
            next_i, next_j = i + shift_i, j + shift_j
            if (
                not is_out_of_field_point(next_i, next_j)
                and field[next_i][next_j] > field[i][j]
                and (next_i, next_j) not in visited
                and field[next_i][next_j] < 9
            ):
                queue.append((next_i, next_j))
                visited.add((next_i, next_j))

    return size


def part1():
    return sum(field[i][j] + 1 for i, j in get_minimal_points())


def part2():
    basins = [get_basin_size(i, j) for i, j in get_minimal_points()]
    a, b, c, *_ = sorted(basins, reverse=True)
    return a * b * c


print(part1())
print(part2())
