def pal(num):
    if num < 0:
        return False
    original = num
    rev = 0
    while num > 0:
        temp = num % 10
        rev = (rev * 10) + temp
        num //= 10

    return rev == original

