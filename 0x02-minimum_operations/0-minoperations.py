#!/usr/bin/python3

def minOperations(n):
    if n <= 1:
        return 0  # If n is 1 or less, no operations are needed.

    operations = 0
    divisor = 2  # Start checking from the smallest prime factor.

    while n > 1:
        # If n is divisible by the current divisor, keep dividing.
        while n % divisor == 0:
            operations += divisor  # Add the divisor to the operations count.
            n //= divisor  # Reduce n.
        divisor += 1  # Move to the next divisor.

    return operations

