def combinations(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:], r-1):
                yield [arr[i]] + next



result = []
for combi in combinations(list(range(8)),3):
    print(combi)

# print(result)
