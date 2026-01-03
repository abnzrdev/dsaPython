class Math:
    # Problem A: Naive solution
    def divisors(self, num):
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        return count - 2  # exclude 1 and num itself

    # Problem A: Efficient solution
    def divisors_efficient(self, num):
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
    def primefactors(self, num):
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
    def sum(self, num):
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

    # Problem D
    def pairs(self, num):
        result = 0
        for i in range(1, num + 1):
            result += num // i
        
        return result

    # Problem E
    def sieve(self, num):
        is_prime = [True for i in range(num + 1)]
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(num ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, num + 1, i):
                    is_prime[j] = False
        
        return  [k for k in range(num + 1) if is_prime[k]]

    # Problem F
    


if __name__ == "__main__":
    math = Math()
    num1, num2 = map(int, input().split())
    siever = math.sieve(num2)
    prime_count = 0
    for i in range(num1, num2 + 1):
        if i in siever:
            prime_count += 1
    print(prime_count)
        
