points = []  # xs, ys, xf, yf
max_x = 0
max_y = 0

with open('input.txt') as input_file:
    for line in input_file.read().split('\n'):
        if not line:
            continue

        start, finish = line.split(' -> ')
        xs, ys = [int(n) for n in start.split(',')]
        xf, yf = [int(n) for n in finish.split(',')]
        max_x = max(max_x, xs, xf)
        max_y = max(max_y, ys, yf)
        points.append([xs, ys, xf, yf])


size_x = max_x + 1
size_y = max_y + 1
field = [[0] * size_x for _ in range(size_y)]

for xs, ys, xf, yf in points:
    if ys == yf:
        for x in range(min(xs, xf), max(xs, xf) + 1):
            field[ys][x] += 1

    elif xs == xf:
        for y in range(min(ys, yf), max(ys, yf) + 1):
            field[y][xs] += 1

    # just comment this condition to get part1 solution
    else:
        for shift in range(abs(xs - xf) + 1):
            shift_y = shift if ys < yf else -shift
            shift_x = shift if xs < xf else -shift
            field[ys + shift_y][xs + shift_x] += 1

res = 0
for i in range(size_x):
    for j in range(size_y):
        if field[i][j] >= 2:
            res += 1

print(res)
