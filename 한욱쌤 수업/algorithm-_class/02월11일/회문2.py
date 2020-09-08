import sys
sys.stdin = open('회문2.txt')

T = 10
for tc in range(T):
    N = int(input())

    arr = [list(input()) for _ in range(100)]
    count = 0
    max_count = 1 # A도 길이가 1인 회문이라고 했으니 ㅇㅅㅇ
    result = 0
    for i in range(100):
        for k in range(101): # 찾을 단어 길이 range
            for j in range(0, 100-k+1):
                for m in range(k//2):
                    if arr[i][j+m] == arr[i][j+k-1-m]:
                        result = 1
                    else:
                        result = 0
                        break
                if result == 1:
                    count = k
            if count > max_count:
                max_count = count


    for i in range(100):
        for k in range(101):
            for j in range(0, 100-k+1):
                for m in range(k//2):
                    if arr[j+m][i] == arr[j+k-1-m][i]:
                        result = 1
                    else:
                        result = 0
                        break
                if result == 1:
                    count = k
            if count > max_count:
                max_count = count

    print("#{} {}".format(N, max_count))