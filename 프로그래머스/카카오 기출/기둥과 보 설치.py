from operator import itemgetter

def check(result):
    for x, y, kind in result:
        # 기둥
        if kind == 0:
            # 바닥인 경우 or 좌측에 보 or  우측에 보 or 밑에 기둥이 있을 경우, 설치 가능한 경우(제거 가능한 경우)
            if y == 0 or (x-1, y, 1) in result or (x, y, 1) in result or (x, y-1, 0) in result:
                continue
            # 설치 못 하는 경우(제거 불가능한 경우)
            else:
                return False
        # 보
        else:
            if (x, y-1, 0) in result or (x+1, y-1, 0) in result or ((x-1, y, 1) in result and (x+1, y, 1) in result):
                continue
            else:
                return False
    return True

def solution(build_frame):
    result = set()
    for a in build_frame:
        x, y, what, install = a
        print(x, y, what, install)
        # 설치
        if install == 1:
            result.add((x, y, what))
            if check(result):
                continue
            else:
                result.remove((x, y, what))
        # 제거
        else:
            if (x, y, what) in result:
                result.remove((x, y, what))
                if check(result):
                    continue
                else:
                    result.add((x, y, what))

    result = [list(i) for i in result]
    print(sorted(result, key=itemgetter(0, 1, 2)))
    print(sorted(result, key=lambda x: (x[0], x[1], x[2])))




T = 1
for tc in range(T):
    build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
    arr = [[2]* 7 for _ in range(6)]

    # result = []
    solution(build_frame)
    # print(arr)

    # for i in build_frame:
    #     a, b, c, d = map(int, i)
    #     temp1 = False
    #     temp2 = ''
    #     if c == 0:
    #         pillar_scan(i)
    #     else:
    #         beam_scan(i)
    #     for j in arr:
    #         print(j, sep='\n')



    # for i in range(7):
    #     for j in range(6):
    #         if arr[6 - j - 1][i] != 2:
    #             result.append([i, j, arr[6 - j - 1][i]])
    # asd = [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
    # print()
    # s = sorted(result, key=itemgetter(0, 2))
    # print(s)
    # print(asd)