def minops(arr):
    res = 0
    for i in range(len(arr) - 1):
        if(arr[i] > arr[i + 1]):
            res += arr[i] - arr[i + 1]
    return res

if __name__ == "__main__":
    answers = []
    test_cases = int(input(""))
    for i in range(test_cases):
        size = int(input(""))
        arr = list(map(int, input("").split()))
        answer = minops(arr)
        answers.append(answer)

    for i in answers:
        print(i)
