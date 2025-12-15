"""
Mathematical operations module for DSA practice.
Contains efficient implementations of common mathematical algorithms.
"""

class MathOperations:
    def is_palindrome(self, num):
        """
        Check if a number is a palindrome.
        Time Complexity: O(log10(n))
        Space Complexity: O(1)

        Args:
            num: Integer to check

        Returns:
            bool: True if palindrome, False otherwise
        """
        if num < 0:
            return False

        original = num
        rev = 0
        while num > 0:
            rev = (rev * 10) + (num % 10)
            num //= 10

        return rev == original

    def factorial(self, num):
        """
        Calculate factorial of a number.
        Time Complexity: O(n)
        Space Complexity: O(1)

        Args:
            num: Non-negative integer

        Returns:
            int: Factorial value, or None if input is invalid
        """
        if num < 0:
            return None

        result = 1
        for i in range(2, num + 1):
            result *= i

        return result

    def count_factorial_digits(self, num):
        """
        Count number of digits in factorial of a number using Kamenetsky's formula.
        Time Complexity: O(1)
        Space Complexity: O(1)

        Args:
            num: Non-negative integer

        Returns:
            int: Number of digits in factorial, or None if input is invalid
        """
        if num < 0:
            return None
        if num <= 1:
            return 1

        import math
        # Kamenetsky's formula:
        # digits = floor( n*log10(n/e) + log10(2*pi*n)/2 ) + 1
        x = num * math.log10(num / math.e) + 0.5 * math.log10(2 * math.pi * num)
        return int(math.floor(x)) + 1

    def count_trailing_zeros_factorial(self, num):
        """
        Count trailing zeros in factorial of a number.
        Trailing zeros are produced by factors of 10 (2 * 5).
        Since factors of 2 are more abundant, we count factors of 5.
        Time Complexity: O(log5(n))
        Space Complexity: O(1)

        Args:
            num: Non-negative integer

        Returns:
            int: Number of trailing zeros in factorial, or None if input is invalid
        """
        if num < 0:
            return None

        count = 0
        power_of_5 = 5
        while num // power_of_5 >= 1:
            count += num // power_of_5
            power_of_5 *= 5

        return count

    def gcd(self, a, b):
        """
        Calculate Greatest Common Divisor using Euclidean algorithm.
        Time Complexity: O(log(min(a, b)))
        Space Complexity: O(1)

        Args:
            a: First integer
            b: Second integer

        Returns:
            int: GCD of a and b
        """
        a, b = abs(a), abs(b)
        while b:
            a, b = b, a % b
        return a

    def lcm(self, a, b):
        """
        Calculate Least Common Multiple.
        Time Complexity: O(log(min(a, b)))
        Space Complexity: O(1)

        Args:
            a: First integer
            b: Second integer

        Returns:
            int: LCM of a and b
        """
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.gcd(a, b)

    def is_prime(self, num):
        """
        Check if a number is prime.
        Time Complexity: O(sqrt(n))
        Space Complexity: O(1)

        Args:
            num: Integer to check

        Returns:
            bool: True if prime, False otherwise
        """
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False

        # Check for divisors up to sqrt(num)
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6

        return True

    def count_divisors(self, num):
        """
        Count the number of divisors of a number.
        Time Complexity: O(sqrt(n))
        Space Complexity: O(1)

        Args:
            num: Positive integer

        Returns:
            int: Number of divisors
        """
        if num <= 0:
            return 0

        count = 0
        i = 1
        while i * i <= num:
            if num % i == 0:
                count += 1 if i * i == num else 2
            i += 1

        return count

    def power(self, base, exp):
        """
        Calculate power using binary exponentiation.
        Time Complexity: O(log(exp))
        Space Complexity: O(1)

        Args:
            base: Base number
            exp: Non-negative exponent

        Returns:
            int: base^exp, or None if exp is negative
        """
        if exp < 0:
            return None

        result = 1
        while exp > 0:
            if exp % 2 == 1:
                result *= base
            base *= base
            exp //= 2

        return result





