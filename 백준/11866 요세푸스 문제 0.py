import sys

N, K = map(int, sys.stdin.readline().split())
my_data = list(range(1, N+1))
NN = N
cnt = 0
idx = 0
key = 1
result = []

while cnt != NN:
    # K배수 찾기
    if key % K == 0:
        result.append(my_data.pop(idx % N))
        # cnt 개수 1개 늘리고 K배수 찾는 변수 초기화
        cnt += 1
        key = 0
        # 인덱스를 현재 length에 맞게 설정
        idx %= N
        idx -= 1
        N -= 1

    idx += 1
    key += 1

print('<', end='')
print(*result, sep=', ', end='')
print('>')