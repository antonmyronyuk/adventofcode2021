def progression_sum(num):
    return num * (num + 1) // 2


with open('input.txt') as input_file:
    line = input_file.read().strip()
    tx, ty = line.replace('target area: ', '').split(', ')
    x_start, x_finish = [int(num) for num in tx.replace('x=', '').split('..')]
    y_start, y_finish = [int(num) for num in ty.replace('y=', '').split('..')]


min_x_velocity = next(
    x for x in range(x_finish)
    if x_start <= progression_sum(x) <= x_finish
)
max_x_velocity = x_finish
min_y_velocity = y_start
max_y_velocity = abs(y_start) - 1


def is_matching_velocity(x_velocity, y_velocity):
    x, y = 0, 0
    while True:
        if x_start <= x <= x_finish and y_start <= y <= y_finish:
            return True

        if x > x_finish or y < y_start:
            return False

        x += x_velocity
        y += y_velocity
        x_velocity -= 1 if x_velocity else 0
        y_velocity -= 1


def get_matching_velocities_count():
    res = 0
    for x_velocity in range(min_x_velocity, max_x_velocity + 1):
        for y_velocity in range(min_y_velocity, max_y_velocity + 1):
            res += is_matching_velocity(x_velocity, y_velocity)

    return res


if __name__ == '__main__':
    print(progression_sum(max_y_velocity))  # part1
    print(get_matching_velocities_count())  # part2
