import math
from heapq import heappop, heappush


def get_field():
    with open('input.txt') as input_file:
        lines = [line for line in input_file.read().split('\n') if line]

    field = []
    for line in lines:
        field.append([int(n) for n in line])

    return field


def get_large_field():
    field = get_field()
    N = len(field)
    M = len(field[0])
    K = 5
    large_field = [[0] * M * K for _ in range(N * K)]
    for ki in range(K):
        for kj in range(K):
            for i in range(N):
                for j in range(M):
                    val = field[i][j] + ki + kj
                    large_field[ki * N + i][kj * M + j] = val % 9 or 9

    return large_field


def get_lowest_total_risk(field):
    N = len(field)
    M = len(field[0])
    risk = [[math.inf] * M for _ in range(N)]

    queue = [(0, (0, 0))]  # heap of (total_risk, (i, j))
    risk[0][0] = 0

    while queue:
        _, (i, j) = heappop(queue)  # point with minimal total risk

        for si, sj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = i + si, j + sj
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue

            new_risk = risk[i][j] + field[ni][nj]
            if risk[ni][nj] > new_risk:
                risk[ni][nj] = new_risk
                heappush(queue, (new_risk, (ni, nj)))

    return risk[N - 1][M - 1]


if __name__ == '__main__':
    print(get_lowest_total_risk(get_field()))  # part 1
    print(get_lowest_total_risk(get_large_field()))  # part 2
