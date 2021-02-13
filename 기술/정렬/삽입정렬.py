N = int(input())
my_list = []

for n in range(N):
    my_list.append(int(input()))
    for i in range(len(my_list)):
        while i > 0 and my_list[i-1] > my_list[i]:
            my_list[i-1], my_list[i] = my_list[i], my_list[i-1]
            i -= 1

print(*my_list, sep='\n')

'''
O(N^2)
정렬 범위를 1칸씩 확장해나가면서 새롭게 정렬 범위에 들어온 값을 기존 값들과 비교하여 알맞은 자리에 꼽아주는 알고리즘
'''