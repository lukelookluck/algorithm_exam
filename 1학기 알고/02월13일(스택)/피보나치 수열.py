import time
startTime = time.time()



# 재귀
def fibo(n):
    if n < 2:
        return n

    while n >= 2:
        return fibo(n-1) + fibo(n-2)

print(fibo(4))
endTime = time.time() - startTime
print(endTime)


startTime2 = time.time()
# 스택 recursive 방식
def fibo1(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]

memo = [0, 1]
print(fibo1(600))
endTime2 = time.time() - startTime2
print(endTime2)


# 스택(더 최적화) iterative 방식
def fibo2(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-2] + f[i-1])
    return f[n]

print(fibo2(600))