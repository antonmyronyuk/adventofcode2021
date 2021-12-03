with open('input.txt') as input_file:
    lines = [line for line in input_file.read().split()]
    commands = lines[::2]
    distances = [int(distance) for distance in lines[1::2]]

x = 0
y = 0

for command, distance in zip(commands, distances):
    if command == 'forward':
        x += distance
    elif command == 'up':
        y -= distance
    elif command == 'down':
        y += distance

print(x * y)
