def solution(a):
    answer = 2
    my_min_left = a[0]
    my_min_right = a[-1]
    for i in range(1, len(a)-1):
        if my_min_left > a[i]:
            my_min_left = a[i]
            answer += 1
        if my_min_right > a[-1 - i]:
            my_min_right = a[-1 - i]
            answer += 1

    if my_min_right == my_min_left:
        answer -= 1
    return answer


print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))