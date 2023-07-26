def sieve_of_eratosthenes(n):
    # Create a list to mark non-prime numbers. Initially, all numbers are assumed prime.
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    # Mark non-prime numbers starting from 2 up to the square root of n.
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # Return a list of prime numbers.
    return [num for num in range(2, n + 1) if is_prime[num]]

# Find all prime numbers between 2 and 100.
primes = sieve_of_eratosthenes(100)

# Print the result.
print("Prime numbers between 2 and 100:")
print(primes)
