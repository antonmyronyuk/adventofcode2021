with open('input.txt') as input_file:
    nums = [int(num) for num in input_file.read().split('\n')[0].split(',')]

SIMULATION_DAYS = 256  # just change this constant to 80 for task part 1
counts = [0] * (SIMULATION_DAYS + 10)
res = len(nums)

# first week counts of new fishes produced
counts[:7] = [sum(num - i == 0 for num in nums) for i in range(7)]

for i in range(SIMULATION_DAYS):
    counts[i + 7] += counts[i]
    counts[i + 9] += counts[i]
    res += counts[i]

print(res)
