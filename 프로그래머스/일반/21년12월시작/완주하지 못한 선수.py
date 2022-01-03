def solution(participant, completion):
    part = {}

    for p in participant:
        if p in part:
            part[p] += 1
        else:
            part[p] = 1

    for c in completion:
        part[c] -= 1

    for p, s in part.items():
        if s != 0:
            return p


p = ["marina", "josipa", "nikola", "vinko", "filipa"]
s = ["josipa", "filipa", "marina", "nikola"]
solution(p, s)