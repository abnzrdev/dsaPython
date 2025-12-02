class Math():
    def pal(self, num):
        if num < 0:
            return False
        original = num
        rev = 0
        while num > 0:
            temp = num % 10
            rev = (rev * 10) + temp
            num //= 10

        return rev == original

    def factorial(self, num):
        if num < 0:
            return False
        result = 1
        while num > 1:
            result *= num
            num -= 1

        return result

    def factorial_dig(self, num):
        if num < 0:
            return False
        fact = self.factorial(num)
        if fact == 0:
            return 1
        count = 0
        while fact > 0:
            fact //= 10
            count += 1

        return count