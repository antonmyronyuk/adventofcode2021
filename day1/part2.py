with open('input.txt') as input_file:
    nums = [int(num) for num in input_file.read().split('\n') if num]

zipped = zip(nums, nums[1:], nums[2:], nums[3:])
res = sum(a + b + c < b + c + d for a, b, c, d in zipped)
print(res)
