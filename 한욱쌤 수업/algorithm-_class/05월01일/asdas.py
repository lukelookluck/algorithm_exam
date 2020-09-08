import sys
sys.stdin = open('암호코드 스캔.txt')
a = []
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    passwords_map = [input() for i in range(N)]
    passwords = ['' for i in range(N)]
    passwords_patterns = {
        '0001101': '0',
        '0011001': '1',
        '0010011': '2',
        '0111101': '3',
        '0100011': '4',
        '0110001': '5',
        '0101111': '6',
        '0111011': '7',
        '0110111': '8',
        '0001011': '9'
    }
    binary_patterns = [0] * 16
    binary_patterns[0] = '0000'
    binary_patterns[1] = '0001'
    binary_patterns[2] = '0010'
    binary_patterns[3] = '0011'
    binary_patterns[4] = '0100'
    binary_patterns[5] = '0101'
    binary_patterns[6] = '0110'
    binary_patterns[7] = '0111'
    binary_patterns[8] = '1000'
    binary_patterns[9] = '1001'
    binary_patterns[10] = '1010'
    binary_patterns[11] = '1011'
    binary_patterns[12] = '1100'
    binary_patterns[13] = '1101'
    binary_patterns[14] = '1110'
    binary_patterns[15] = '1111'
    changing = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    max_sum = 0
    asd = 0
    for i in range(N):
        for j in range(M):
            if passwords_map[i][j] <= '9':
                passwords[i] += binary_patterns[int(passwords_map[i][j])]
            else:
                passwords[i] += binary_patterns[changing[passwords_map[i][j]]]
    sum_sum = 0
    for i in range(N):
        if passwords[i].strip('0'):
            print(passwords[i].strip('0'))
    for i in range(1, N):
        j = M * 4 - 1
        output = ''
        while j > 0:
            if passwords[i][j] != '0' and passwords[i-1][j] != passwords[i][j]:
                x, y, z = 0, 0, 0
                while passwords[i][j] == '1':
                    x += 1
                    j -= 1
                while passwords[i][j] == '0':
                    y += 1
                    j -= 1
                while passwords[i][j] == '1':
                    z += 1
                    j -= 1
                d = min(x, y, z)
                x = x // d
                y = y // d
                z = z // d
                pattern = ''
                for k in range(7 - (x + y + z)):
                    pattern += '0'
                for k in range(z):
                    pattern += '1'
                for k in range(y):
                    pattern += '0'
                for k in range(x):
                    pattern += '1'
                output += passwords_patterns[pattern]
            j = j - 1
            if len(output) == 8:

                result = 0
                ans = 0
                for k in range(7, -1, -1):
                    if not k & 1:
                        result += int(output[k])
                        ans += int(output[k])
                    else:
                        result += int(output[k]) * 3
                        ans += int(output[k])
                if result % 10 == 0:
                    sum_sum += ans
                    print("{} {}".format(asd + 1, output))
                    a.append(output)
                    asd += 1
                output = ''
    print('#{} {}'.format(tc, sum_sum))
    print(a)