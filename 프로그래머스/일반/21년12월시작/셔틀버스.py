def solution(n, t, m, timetable):
    answer = 0
    tt, bt = [], []

    for time in timetable:
        tt.append(int(time[:2]) * 60 + int(time[-2:]))

    tt.sort(reverse=True)

    for i in range(n):
        bt.append(540 + i * t)

    cnt = 0
    while cnt < n:
        temp = []
        m_c = 0
        while m_c != m:
            if tt and tt[-1] <= bt[cnt]:
                m_c += 1
                temp.append(tt.pop())
            else:
                break

        if cnt == n - 1:
            if m_c == m:
                answer = temp.pop() - 1
            else:
                answer = bt[-1]

        cnt += 1

    h = '0' + str(answer // 60) if (answer // 60) < 10 else answer // 60
    m = '0' + str(answer % 60) if (answer % 60) < 10 else answer % 60

    return str(h) + ':' + str(m)