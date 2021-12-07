with open('input.txt') as input_file:
    nums = [int(num) for num in input_file.read().split('\n')[0].split(',')]


def progression_sum(n):
    return n * (n + 1) // 2


def part1():
    return min(
        sum(abs(num - d) for num in nums)
        for d in range(min(nums), max(nums) + 1)
    )


def part2():
    return min(
        sum(progression_sum(abs(num - d)) for num in nums)
        for d in range(min(nums), max(nums) + 1)
    )


print(part1())
print(part2())
