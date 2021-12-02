with open('input.txt') as input_file:
    nums = [int(num) for num in input_file.read().split('\n') if num]

res = sum(prev < cur for prev, cur in zip(nums, nums[1:]))
print(res)
