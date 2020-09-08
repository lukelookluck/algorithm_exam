total = 0
N = 10
A = [0 for _ in range(N)] # 원소 포함 여부 저장 0 , 1
data = list(range(1, 11))

def print_set(n):
    count = 0
    for i in range(n):   #각 부분 배열의 원소 출력
        if A[i] == 1:  # A[i]가 1이면 포함된 것으로 출력
            count += data[i]

    if count == 10:
        for i in range(n):  # 각 부분 배열의 원소 출력
            if A[i] == 1:  # A[i]가 1이면 포함된 것으로 출력
                print(data[i], end=' ')
        print()

def power_set(n, k): # n: 원소의 갯수, k: 현재 depth
    global total
    total += 1
    if n == k:  # Basic Part
        print_set(n)
    else:       # inductive part
        A[k] = 1    # k번 요소 O
        power_set(n, k+1)   # 다음 요소 포함 여부 결정
        A[k] = 0    # k번 요소 X
        power_set(n, k+1) # 다음 요소 포함 여부 결정


power_set(10, 0)
print("호출회수 : {}".format(total))