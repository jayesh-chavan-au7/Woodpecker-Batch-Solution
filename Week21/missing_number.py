arr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]
brr = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]


def missingNumbers(arr, brr):
    indexLength = max(arr+brr)
    table = [0 for i in range(indexLength+1)]

    for i in arr:
        table[i] += 1

    for j in brr:
        table[j] -= 1

    return [i for i in range(len(table)) if table[i] != 0]


if __name__ == '__main__':
    # n = int(input())
    # arr = list(map(int, input().rstrip().split()))
    # m = int(input())
    # brr = list(map(int, input().rstrip().split()))
    result = missingNumbers(arr, brr)
    print(result)
