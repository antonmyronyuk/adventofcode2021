with open('input.txt') as input_file:
    NUMS = [num for num in input_file.read().split('\n') if num]
    SIZE = len(NUMS[0])


def most_common(nums, pos) -> str:
    zeros = sum(num[pos] == '0' for num in nums)
    ones = sum(num[pos] == '1' for num in nums)
    return '1' if ones >= zeros else '0'


def invert_num(num) -> str:
    return ''.join('1' if char == '0' else '0' for char in num)


res = ''.join(most_common(NUMS, i) for i in range(SIZE))
inverted = invert_num(res)

a = int(res, 2)
b = int(invert_num(res), 2)
print(a * b)
