"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isPrime(number):
    if number == 1:
        return False

    for n in range (2, int(number ** 0.5) + 1):
        if number%n == 0:
            return False

    return True

def primes(number_of_primes):
    list = []
    iteration = 0

    if number_of_primes <= 0:
        raise ValueError("Positive numbers only.")

    while (len(list) < number_of_primes):
        iteration += 1
        if isPrime(iteration):
            list.append(iteration)

    return list
