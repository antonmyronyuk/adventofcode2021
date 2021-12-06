with open('input.txt') as input_file:
    nums = [int(num) for num in input_file.read().split('\n')[0].split(',')]

SIMULATION_DAYS = 256  # just change this constant to 80 for task part 1
next_counts = [0] * (SIMULATION_DAYS + 10)
res = len(nums)

# how many new fishes will be produced after 7 days
eights_count = [sum(num - i == 0 for num in nums) for i in range(7)]

for i in range(SIMULATION_DAYS):
    eights_count[i % 7] += next_counts[i]
    next_counts[i + 9] += eights_count[i % 7]
    res += eights_count[i % 7]

print(res)
