import sys

def solution(x, y, z):
    if x <= 0 or y <= 0 or z <= 0:
        return 1

    if x > 20 or y > 20 or z > 20:
        return solution(20, 20, 20)

    if check[x][y][z]:
        return check[x][y][z]

    if x < y < z:
        check[x][y][z] = solution(x, y, z-1) + solution(x, y-1, z-1) - solution(x, y-1, z)
        return check[x][y][z]

    else:
        check[x][y][z] = solution(x-1, y, z) + solution(x-1, y-1, z) + solution(x-1, y, z-1) - solution(x-1, y-1, z-1)
        return check[x][y][z]


check = [[[0] * 21 for _ in range(21)] for _ in range(21)]

while True:
    x, y, z = map(int, sys.stdin.readline().split())

    if x == y == z == -1:
        break
    print(f'w({x}, {y}, {z}) = {solution(x,y,z)}')



