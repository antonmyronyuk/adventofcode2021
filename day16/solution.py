import operator
from functools import reduce

PACK_TYPE_TO_OPERATOR = {
    0: sum,
    1: lambda args: reduce(operator.mul, args),
    2: min,
    3: max,
    5: lambda args: int(operator.gt(*args)),
    6: lambda args: int(operator.lt(*args)),
    7: lambda args: int(operator.eq(*args)),
}


def hex_to_bin(char):
    return bin(int(char, 16))[2:].zfill(4)


class Parser:
    def __init__(self, string):
        self.rest = ''.join(hex_to_bin(char) for char in string)

    def get_pack_type4_value(self):
        code = ''
        while True:
            last_digit = self.rest[0] == '0'
            code += self.rest[1:5]
            self.rest = self.rest[5:]
            if last_digit:
                break

        return int(code, 2)

    def get_pack_l0_sub_packs(self):
        sub_packages_length = int(self.rest[:15], 2)
        self.rest = self.rest[15:]
        sub_packs = []
        used_length = 0
        while used_length < sub_packages_length:
            rest_length_before = len(self.rest)
            sub_packs.append(self.get_pack())
            used_length += rest_length_before - len(self.rest)

        return sub_packs

    def get_pack_l1_sub_packs(self):
        sub_packs_count = int(self.rest[:11], 2)
        self.rest = self.rest[11:]
        return [self.get_pack() for _ in range(sub_packs_count)]

    def get_pack(self):
        pack_version = int(self.rest[:3], 2)
        pack_type = int(self.rest[3:6], 2)
        self.rest = self.rest[6:]
        if pack_type == 4:
            return [pack_version, pack_type, self.get_pack_type4_value()]

        pack_l = self.rest[0]
        self.rest = self.rest[1:]
        if pack_l == '0':
            sub_packs = self.get_pack_l0_sub_packs()
        else:
            sub_packs = self.get_pack_l1_sub_packs()

        return [pack_version, pack_type, sub_packs]


def calc_part1(pack):
    pack_version, pack_type, pack_value = pack
    if pack_type == 4:
        return pack_version

    return pack_version + sum(calc_part1(sub_pack) for sub_pack in pack_value)


def calc_part2(pack):
    _, pack_type, pack_value = pack
    if pack_type == 4:
        return pack_value

    args = [calc_part2(sub_pack) for sub_pack in pack_value]
    return PACK_TYPE_TO_OPERATOR[pack_type](args)


if __name__ == '__main__':
    with open('input.txt') as input_file:
        line = input_file.read().strip()

    pack = Parser(line).get_pack()
    print(calc_part1(pack))
    print(calc_part2(pack))
