import sys
sys.stdin = open('배열 최소 합.txt')

def my_func():
    result = []
    except_column = [0]
    except_column2 = [0]
    for i in range(N):
        min_num = 10
        # print("--")
        for j in range(1, N+1):
            if min_num > arr[i][j] and j not in except_column2:
                min_num = arr[i][j]
                except_column.append(j)
                # print(except_column)
                # print("___")
        except_column2.append(except_column[-1])
        result.append(min_num)
        # print("***")
        # print(except_column2)
        # print("***")
        # print(result)
        # print("~~~")
    count = 0
    for i in result:
        count += i
    return count

def my_func2():
    result = []
    except_column = [0]
    except_column2 = [0]
    for i in range(N):
        min_num = 10
        # print("--")
        for j in range(1, N+1):
            if min_num >= arr[i][j] and j not in except_column2:
                min_num = arr[i][j]
                except_column.append(j)
                # print(except_column)
                # print("___")
        except_column2.append(except_column[-1])
        result.append(min_num)
        # print("***")
        # print(except_column2)
        # print("***")
        # print(result)
        # print("~~~")
    count = 0
    for i in result:
        count += i
    return count

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [[0] + list(map(int, input().split())) for _ in range(N)]
    # print(arr)




    a = []
    a.append(my_func())
    a.append(my_func2())
    print("#{} {}".format(tc+1, min(a)))