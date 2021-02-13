def solution(n):
    my_arr = [[[] for _ in range(i)] for i in range(1, n+1)]
    cnt = 0
    cnt2 = 0
    digit = 1

    for i in range(1, n+1):
        for j in range(n-i+1):
            if i % 3 == 1:
                cnt += 1
                my_arr[cnt-1][cnt2 // 3] = digit
            elif i % 3 == 2:
                my_arr[cnt-1][j+1 + cnt2 // 3] = digit
            else:
                cnt -= 1
                my_arr[cnt - 1][cnt-1 - cnt2 // 3] = digit
            digit += 1

        cnt2 += 1

    answer = []

    for i in my_arr:
        answer += i
    return answer


print(solution(5))