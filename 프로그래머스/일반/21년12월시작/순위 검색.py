from collections import defaultdict

lang = ['cpp', 'java', 'python']
part = ['backend', 'frontend']
care = ['junior', 'senior']
food = ['chicken', 'pizza']

def solution(info, query):
    answer = []
    my_d = defaultdict(dict)
    
    def search(a, b, c, d, e):
        cnt = 0
        if a == '-':
            for t in lang:
                cnt += search(t, b, c, d, e)
        elif b == '-':
            for t in part:
                cnt += search(a, t, c, d, e)
        elif c == '-':
            for t in care:
                cnt += search(a, b, t, d, e)
        elif d == '-':
            for t in food:
                cnt += search(a, b, c, t, e)
        else:
            l, h = 0, len(my_d[a][b][c][d]) - 1
            result = len(my_d[a][b][c][d])
            while l <= h:
                m = (l + h) // 2
                if e > my_d[a][b][c][d][m]:
                    l = m + 1
                else:
                    result = m
                    h = m - 1
            cnt += len(my_d[a][b][c][d])  - result
        return cnt            
        
                
    for l in lang:
        my_d[l] = {}
        for p in part:
            my_d[l][p] = {}
            for c in care:
                my_d[l][p][c] = {}
                for f in food:
                    my_d[l][p][c][f] = []
                    
    for temp in info:
        a, b, c, d, e = temp.split()
        my_d[a][b][c][d].append(int(e))
                    
    for a in lang:
        for b in part:
            for c in care:
                for d in food:
                    my_d[a][b][c][d].sort()        
    
    for temp in query:
        a, b, c, d = temp.split(' and ')
        d, e = d.split()
        e = int(e)
        # print(a, b, c, d, e)
        answer.append(search(a, b, c, d, e))
    
    
    
    
    return answer
