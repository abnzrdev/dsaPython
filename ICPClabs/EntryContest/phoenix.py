def phoenix(n, k, arr):
    unique = list(set(arr))
    if len(unique) > k:
        return -1
    while len(unique) < k:
        unique.append(1)
    res = []
    for i in range(n):
        res.extend(unique)
    return res

if __name__ == "__main__":
    test_cases = int(input(""))
    results = []
    for i in range(test_cases):
        n, k = map(int, input("").split())
        arr = list(map(int, input().split()))
        result = phoenix(n, k, arr)
        results.append(result)
    print(results)