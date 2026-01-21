def cipher(string_inp, num):
    i = 0
    result = " "
    while i < num:
        result += string_inp[i]
        i += len(result)
    return result

if __name__ == "__main__":
    num = int(input(""))
    string_input = input("")
    print(cipher(string_input, num))