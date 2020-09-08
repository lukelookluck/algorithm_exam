import sys
sys.stdin = open('다솔이의 다이아몬드 장식.txt')

T = int(input())
for tc in range(T):
    str = input()

    print("."+".#.."*len(str))
    print("."+"#."*len(str)*2)
    print("#", end='')
    for i in str:
        print(".{}.#".format(i), end='')
    print()
    print("." + "#." * len(str) * 2)
    print("." + ".#.." * len(str))