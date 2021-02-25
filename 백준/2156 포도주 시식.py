import sys

def solution(idx, mybool, result):
    if idx >= n:
        print('악',result)
        return
    # print(idx, mybool)
    if mybool is True:
        solution(idx+1, False, result + str(data[idx+1]))
        solution(idx+2, True, result + str(data[idx+2]))
    else:
        solution(idx+3, True, result + str(data[idx+3]))
        solution(idx+2, True, result + str(data[idx+2]))


n = int(sys.stdin.readline().strip())
data = []

for _ in range(n):
    data.append(int(sys.stdin.readline().strip()))

data.append('aa')
data.append('asdasd')
data.append('zzz')

solution(0, True, str(data[0]))
solution(1, True, str(data[1]))