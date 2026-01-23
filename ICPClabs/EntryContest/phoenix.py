def phoenix(n, k, arr):
    unique = []
    for x in arr:
        if x not in unique:
            unique.append(x)
    if len(unique) > k:
        return -1
    while len(unique) < k:
        unique.append(1)
    res = []
    for _ in range(n):
        res.extend(unique)
    return res

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        res = phoenix(n, k, arr)
        if res == -1:
            print(-1)
        else:
            print(len(res))
            print(res)