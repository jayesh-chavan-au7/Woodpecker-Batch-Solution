def icecreamParlor(m, arr):
    result = []
    for i in range(len(arr)):
        x = arr[i+1:]
        for j in range(len(x)):
            if arr[i]+x[j] == m:
                result.append(i+1)
                result.append(j+i+2)
                return result


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)
        print(result)
