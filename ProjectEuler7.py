# By listing the first six prime numbers:  2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.  

# What is the 10001st prime number?


import time
import math

start = time.time()
##########################################
def is_prime(number):
    max = int(math.sqrt(number)) + 1

    if number == 2:
        return True

    if number % 2 != 0:
        for x in range(3, max, 2):
            if number%x == 0:
                return False
    else:
        return False
    return True

still_looking = True
counter = 1 # We have found 1 prime at the beginning (assume 2)
number = 3

while still_looking:
    if is_prime(number):
        counter += 1
    
    if counter == 10001:
        still_looking = False
        answer = number

    number += 2
##########################################
finish = time.time()

print(answer)
print(finish - start)