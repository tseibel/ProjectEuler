import math

def sieve_of_eratosthenes(n):
    """
    1. Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
    2. Initially, let p equal 2, the smallest prime number.
    3. Enumerate the multiples of p by counting in increments of p from 2p to n, and mark them in the list (these will be 2p, 3p, 4p, ...; the p itself should not be marked).
    4. Find the smallest number in the list greater than p that is not marked. If there was no such number, stop. Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.
    5. When the algorithm terminates, the numbers remaining not marked in the list are all the primes below n.
    """
    primes = [True] * (n-1)
    prime = 2 # 

    while prime <= n:
        if primes[prime-2]:
            for number in range(prime * 2, n, prime):
                primes[number - 2] = False
        
        prime +=1

    return primes


def divisors(number):
    print(number)

def count_divisors(number):
    divisors = 0

    if number == 1:
        return 1

    for x in range(1, int(math.sqrt(number)) + 1, 1):
        if number%x == 0: 
            if math.sqrt(number) == x:
                divisors+=1
            else:
                divisors += 2
            
    return divisors

def is_even(value):
    if value == 1:
        return False
    
    if value%2 == 0:
        return True

    else:
        return False
