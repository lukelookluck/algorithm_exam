def solution(n, lost, reserve):
    my_re = {r for r in reserve if r not in sorted(lost)}
    my_lo = {l for l in lost if l not in sorted(reserve)}
    
    for r in my_re:
        if r - 1 in my_lo:
            my_lo.discard(r - 1)
        elif r + 1 in my_lo:
            my_lo.discard(r + 1)
    
    return n - len(my_lo)
