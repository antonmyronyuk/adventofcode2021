import typing as t

N = 5


class Number:
    def __init__(self, number):
        self.number = number
        self.marked = False


class Board:
    def __init__(self, numbers: t.List[t.List[Number]]):
        self.numbers = numbers

    def is_winning(self) -> bool:
        for i in range(N):
            if all(self.numbers[i][j].marked for j in range(N)):
                return True

        for i in range(N):
            if all(self.numbers[j][i].marked for j in range(N)):
                return True

        return False

    def mark_number(self, number):
        for i in range(N):
            for j in range(N):
                if self.numbers[i][j].number == number:
                    self.numbers[i][j].marked = True

    def unmarked_score(self) -> int:
        score = 0
        for i in range(N):
            for j in range(N):
                if not self.numbers[i][j].marked:
                    score += self.numbers[i][j].number

        return score


with open('input.txt') as input_file:
    nums = [int(num) for num in input_file.readline().split(',')]
    lines = [line for line in input_file.read().split('\n') if line]

boards = []
for i in range(len(lines) // 5):
    numbers = []
    for k in range(N):
        index = i * N + k
        numbers.append([Number(int(n)) for n in lines[index].split()])

    boards.append(Board(numbers))


def get_first_winner_score():
    for num in nums:
        for board in boards:
            board.mark_number(num)
            if board.is_winning():
                return board.unmarked_score() * num


def get_last_winner_score():
    winner_board_ids = set()
    for num in nums:
        for i, board in enumerate(boards):
            if i in winner_board_ids:
                continue

            board.mark_number(num)
            if board.is_winning():
                if len(boards) - len(winner_board_ids) > 1:
                    winner_board_ids.add(i)
                else:
                    return board.unmarked_score() * num


print(get_first_winner_score())     # part 1
print(get_last_winner_score())      # part 2
