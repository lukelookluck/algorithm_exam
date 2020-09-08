import sys
sys.stdin = open('a.txt')

T = int(input())

def sequentialsort(data):
    for i in range(0, L - 1, 2):
        max = i
        for j in range(i + 1, L):
            if data[max] < data[j]:

                data[i], data[j] = data[j], data[i]
    for i in range(1, L - 1, 2):
        min = i
        for j in range(i + 1, L):
            if data[min] > data[j]:
                data[i], data[j] = data[j], data[i]



for tc in range(T):
    L = int(input())
    data = list(map(int, input().split()))
    sequentialsort(data)
    data = data[0:10]

#for i in range(10):
    #print(data[i], end= " ")

    # result = data[1:-1]

    print("#{} {}".format(tc+1, ' '.join(map(str, data))))

