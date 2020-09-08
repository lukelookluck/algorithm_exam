def selectionSort(a):
    for i in range(0, len(a)-1): # len(a)-1는 j가 i+1에서 시작하기때문.
         min = i
         for j in range(i+1, len(a)):
             if a[min] > a[j]:

                 a[i], a[j] = a[j], a[i]

def selection(a, k):
    for i in range(0, k): # len(a)-1는 j가 i+1에서 시작하기때문.
         min = i
         for j in range(i+1, len(a)):
             if a[min] > a[j]:
                 min = j
                 a[i], a[min] = a[min], a[i]
    return a[k-1]


data = [126, 215, 156, 12, 78, 8, 1]
selectionSort(data)

# print(selection(data, 3))

print(data)