class Math:
    # Problem A: Naive solution
    def divisors(self, num: int) -> int:
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        return count - 2  # exclude 1 and num itself

    # Problem A: Efficient solution
    def divisors_efficient(self, num: int) -> int:
        count = 0
        i = 1
        while i * i <= num:
            if num % i == 0:
                if i * i == num:  # perfect square
                    count += 1
                else:
                    count += 2
            i += 1
        return count - 2  # exclude 1 and num itself

    # Problem B: Prime factorization
    def primefactors(self, num: int) -> list[tuple[int, int]]:
        factors = []

        # Step 1: factor out 2
        count = 0
        while num % 2 == 0:
            num //= 2
            count += 1
        if count > 0:
            factors.append((2, count))

        # Step 2: factor out odd numbers
        i = 3
        while i * i <= num:
            count = 0
            while num % i == 0:
                num //= i
                count += 1
            if count > 0:
                factors.append((i, count))
            i += 2

        # Step 3: if num is prime > 2
        if num > 1:
            factors.append((num, 1))

        return factors

    # Problem C : Sums
    def sum(self, num: int) -> list[int] | None:
        k = 2
        result = []
        while k < num:
            a = (2 * num - k * (k - 1)) / (2 * k)
            if a > 0 and a.is_integer():
                for i in range(k):
                    result.append(int(a))
                    a += 1
                return result
            k += 1
        return None

    # Problem D : Stepan and pairs
    def pairs(self, num: int) -> int:
        result = 0
        for i in range(1, num + 1):
            result += num // i
        
        return result

    # Problem E : Sieve of Eratosthenes
    def sieve(self, num: int) -> list[int]:
        is_prime = [True for i in range(num + 1)]
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(num ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, num + 1, i):
                    is_prime[j] = False
        
        return  [k for k in range(num + 1) if is_prime[k]]

    # Problem G : Almost Prime
    def is_prime(self, num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def almost_prime(self, low: int, high: int) -> int:
        seen = set()
        for p in range(2, int(high ** 0.5) + 1):
            if self.is_prime(p):
                power = p * p
                while power <= high:
                    if power >= low:
                        seen.add(power)
                    power *= p
        return len(seen)

   # Problem H : Fast Exponentiation
    def fst_expo(self, num: int) -> str:
        binary = str(bin(num))
        result = ""
        for i in range(2, len(binary)):
            if binary[i] == "1":
                result += "SX"
            else:
                result += "S"
        return result
    def gcd(self, num1: int, num2: int) -> int:
        num1, num2 = abs(num1), abs(num2)
        while num2:
            num1, num2 = num2, num1 % num2
        return num1

    def relative_prime(self, num: int) -> int:
        count = 0
        for i in range(1, num + 1):
            if self.gcd(num, i) == 1:
                count += 1
        return count

    # Problem J : Totient Calculator
    def totient_calc(self, num: int) -> float:
        prime_facts = self.primefactors(num)
        factors = []
        indx = 0
        for tup in prime_facts:
            factors.append(tup[indx])

        totient = num
        for i in factors:
            totient *= (1 - (1 / i))

        return totient


if __name__ == "__main__":
    math = Math()
    num1 = int(input("Enter a number : "))
    totient = int(math.totient_calc(num1))
    print(totient)
        
