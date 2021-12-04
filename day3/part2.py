with open('input.txt') as input_file:
    NUMS = [num for num in input_file.read().split('\n') if num]
    SIZE = len(NUMS[0])


def most_common(nums, pos) -> str:
    zeros = sum(num[pos] == '0' for num in nums)
    ones = sum(num[pos] == '1' for num in nums)
    return '1' if ones >= zeros else '0'


def get_oxygen_generator_rating():
    nums_left = NUMS
    for i in range(SIZE):
        nums_left = [
            num for num in nums_left
            if num[i] == most_common(nums_left, i)
        ]

    return nums_left[0]


def get_co2_scrubber_rating():
    nums_left = NUMS
    last_skipped_num = None
    for i in range(SIZE):
        next_nums_left = []
        for num in nums_left:
            if num[i] == most_common(nums_left, i):
                last_skipped_num = num
            else:
                next_nums_left.append(num)

        nums_left = next_nums_left

    return last_skipped_num


a = int(get_oxygen_generator_rating(), 2)
b = int(get_co2_scrubber_rating(), 2)
print(a * b)
