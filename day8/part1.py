with open('input.txt') as input_file:
    res = 0
    lines = [line for line in input_file.read().split('\n') if line]
    for line in lines:
        digits = line.split(' | ')[1].split(' ')
        res += sum(len(digit) in (2, 3, 4, 7) for digit in digits)

print(res)
