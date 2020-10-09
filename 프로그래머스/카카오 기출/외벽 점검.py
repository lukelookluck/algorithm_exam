from collections import deque
import itertools

def solution(n, weak, dist):
    # 탐색거리가 긴 순서대로
    dist.sort(reverse=True)
    weak = deque(weak)
    for i in range(1,len(dist)+1):
        # i:투입할 친구 수와 관련이 있다.
        # 1명만 투입했을 때
        if i==1:
            for _ in range(len(weak)):
                d = dist[0]
                if weak[-1] <= weak[0] + d:
                    return 1
                else:
                    # 커버 안 되면 weak의 그 다음 인덱스 탐색, len(weak)만큼 돔
                    weak.append(weak.popleft() + n)
            ## len(weak)만큼 다 돌리면 weak 원상복구
            weak = deque(map(lambda x:x%n, weak))
        # 2명 이상
        else:
            # 탐색거리 순열리스트 만들기
            dist_2 = list(itertools.permutations(dist[:i]))
            # 순열리스트 중 1개씩 뽑기
            for select_set in dist_2:
                print(select_set)
                print(weak)
                # len(weak) 길이만큼 돌기
                for _ in range(len(weak)):
                    # 탐색거리 계산 인덱스
                    start_index = 0
                    # 현재 인덱스
                    present_index = 0
                    # 뽑은 순열 중 숫자 하나 뽑기
                    for d in select_set:
                        # 탐색 가능한 거리 설정
                        check_length = weak[start_index] + d
                        for idx in range(start_index, len(weak)):
                            # 탐색 가능한 거리보다 클 경우, 탐색거리 계산 인덱스를 현재 인덱스로 바꿔주고 다음 숫자로 탐색
                            if weak[idx] > check_length:
                                start_index = idx
                                break
                            # 탐색 가능한 거리일 경우, 현재 인덱스 업데이트
                            else:
                                present_index = idx
                    # 현재 인덱스가 len(weak)일 경우, 탐색이 가능하다는 말이므로 현재 명ㅂ 출력
                    if present_index == len(weak) -1:
                        return i
                    # 탐색이 불가능하면 weak의 그 다음 인덱스 탐색, len(weak)만큼 돔
                    weak.append(weak.popleft() + n)
                ## len(weak)만큼 다 돌리면 weak 원상복구
                weak = deque(map(lambda x:x%n, weak))
    return -1

n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
print(solution(n, weak, dist))