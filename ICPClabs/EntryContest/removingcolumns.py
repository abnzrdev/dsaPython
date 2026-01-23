def rem_cols(strings):
    if not strings:
        return 0
    n = len(strings)
    m = len(strings[0])
    removed = 0
    sorted_pair = [False] * (n - 1)

    for col in range(m):
        should_remove = False
        for i in range(n - 1):
            if not sorted_pair[i] and strings[i][col] > strings[i + 1][col]:
                should_remove = True
                break
        if should_remove:
            removed += 1
            continue
        for i in range(n - 1):
            if not sorted_pair[i] and strings[i][col] < strings[i + 1][col]:
                sorted_pair[i] = True
    return removed

if __name__ == "__main__":
    test_case, string_length  = map(int, input("").split())
    string_inputs = []
    for i in range(test_case):
        string_input = input("")
        string_inputs.append(string_input)
    print(rem_cols(string_inputs))
