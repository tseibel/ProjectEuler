# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17

# Find the sum of all the primes below two million.

import time
import math

from functions import sieve_of_eratosthenes

start = time.time()
##########################################

n = 2000000
answer_list = sieve_of_eratosthenes(n)
answer = sum([i for i in range(2, n) if answer_list[i-2]])

##########################################
finish = time.time()

print(answer)
print(finish - start)
