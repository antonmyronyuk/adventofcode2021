import math
from copy import deepcopy

with open('input.txt') as input_file:
    lines = input_file.read().strip().split('\n')
    nums = [eval(line) for line in lines]


def recursive_inc_left_bound(left, val):
    if isinstance(left[-1], list):
        recursive_inc_left_bound(left[-1], val)
    else:
        left[-1] += val


def recursive_inc_right_bound(right, val):
    if isinstance(right[0], list):
        recursive_inc_right_bound(right[0], val)
    else:
        right[0] += val


def process_explode(cur, left=None, right=None, parent=None, depth=0):
    a, b = cur
    if isinstance(a, list):
        process_explode(a, left=left, right=cur, parent=cur, depth=depth + 1)
    if isinstance(b, list):
        process_explode(b, left=cur, right=right, parent=cur, depth=depth + 1)
    if depth >= 4:
        if left:
            if left == parent:
                left[1] = 0
            if isinstance(left[0], list):
                recursive_inc_left_bound(left[0], a)
            else:
                left[0] += a

        if right:
            if right == parent:
                right[0] = 0
            if isinstance(right[1], list):
                recursive_inc_right_bound(right[1], b)
            else:
                right[1] += b


def process_split_once(cur, parent=None):
    if isinstance(cur, list):
        a, b = cur
        if process_split_once(a, cur):
            return True
        if process_split_once(b, cur):
            return True

    elif cur >= 10:
        splitted = [math.floor(cur / 2), math.ceil(cur / 2)]
        if parent[0] == cur:
            parent[0] = splitted
        else:
            parent[1] = splitted

        return True


def add_nums(a, b):
    prev = []
    cur = deepcopy([a, b])
    while prev != cur:
        prev = deepcopy(cur)
        process_explode(cur)
        process_split_once(cur)

    return cur


def get_magnitude(num):
    if isinstance(num, int):
        return num

    a, b = num
    return 3 * get_magnitude(a) + 2 * get_magnitude(b)


def get_total_magnitude(nums):
    total = nums[0]
    for num in nums[1:]:
        total = add_nums(total, num)

    return get_magnitude(total)


def get_max_magnitude(nums):
    max_magnitude = 0
    for i, a in enumerate(nums):
        for j, b in enumerate(nums):
            if i == j:
                continue

            max_magnitude = max(max_magnitude, get_magnitude(add_nums(a, b)))

    return max_magnitude


if __name__ == '__main__':
    print(get_total_magnitude(nums))  # part 1
    print(get_max_magnitude(nums))  # part 2
