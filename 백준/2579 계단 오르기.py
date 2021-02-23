import sys

def solution(idx, my_bool, result):
    global answer
    if idx == N-1:
        if result > answer:
            answer = result
        return

    if my_bool:
        if idx + 2 >= N - 1:
            solution(N-1, True, result+myarr[N-1])
        else:
            solution(idx+1, False, result+myarr[idx+1])
            solution(idx+2, True, result+myarr[idx+2])
    else:
        solution(idx+2, True, result+myarr[idx+2])



N = int(sys.stdin.readline().strip())
myarr = []
answer = 0

for _ in range(N):
    myarr.append(int(sys.stdin.readline().strip()))

solution(0, True, myarr[0])
solution(1, True, myarr[1])
print(answer)