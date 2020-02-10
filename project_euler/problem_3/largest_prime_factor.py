import math

def largest_prime_factor(n: int) -> int:
    n_sqrt = math.sqrt(n)
    largest = 2

    while n % largest == 0:
        n = n // largest
    
    largest = 3
    while largest + 2 <= n_sqrt:
        while n % largest == 0:
            n = n // largest
        largest += 2
    return largest

