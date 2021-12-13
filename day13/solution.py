points = []
folds = []

with open('input.txt') as input_file:
    lines = [line for line in input_file.read().split('\n') if line]
    for line in lines:
        if line.startswith('fold'):
            axis, val = line.replace('fold along ', '').split('=')
            folds.append((axis, int(val)))
        else:
            x, y = [int(val) for val in line.split(',')]
            points.append((x, y))

x_max_fold = next(val for axis, val in folds if axis == 'x')
y_max_fold = next(val for axis, val in folds if axis == 'y')
x_max = x_max_fold * 2 + 1
y_max = y_max_fold * 2 + 1

field = [[0] * x_max for _ in range(y_max)]

for x, y in points:
    field[y][x] = 1


def part1():
    res = 0
    axis, _ = folds[0]
    if axis == 'x':
        for y in range(y_max):
            for x in range(x_max // 2):
                res += max(field[y][x], field[y][x_max - 1 - x])
    else:
        for y in range(y_max // 2):
            for x in range(x_max):
                res += max(field[y][x], field[y_max - 1 - y][x])

    print(res)


def part2():
    cur_x_max = x_max
    cur_y_max = y_max
    for axis, _ in folds:
        if axis == 'x':
            for y in range(cur_y_max):
                for x in range(cur_x_max // 2):
                    field[y][x] = max(field[y][x], field[y][cur_x_max - 1 - x])
            cur_x_max = cur_x_max // 2
        else:
            for y in range(cur_y_max // 2):
                for x in range(cur_x_max):
                    field[y][x] = max(field[y][x], field[cur_y_max - 1 - y][x])
            cur_y_max = cur_y_max // 2

    print_field(cur_x_max, cur_y_max)


def print_field(x_max, y_max):
    for y in range(y_max):
        for x in range(x_max):
            print('# ' if field[y][x] == 1 else '  ', end='')
        print()


if __name__ == '__main__':
    part1()
    part2()
