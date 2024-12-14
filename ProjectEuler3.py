# The prime factors of 13915 are 5,7,13,29

# What is the largest prime factor of 600851475143

import time
import math

start = time.time()
##########################################

def is_prime(x):
    current = 2
    upper = int(math.sqrt(x))

    while current <= upper:
        if x % current == 0:
            return False
        current += 1

    return True

def is_factor(value, factor):
    if value % factor == 0:
        return True
    else:
        return False

number = 600851475143
counter = 2
max_factor = 0

while number/counter > math.sqrt(number):
    if number%counter == 0:

        if is_prime(number/counter) and (number/counter > max_factor):
            max_factor = number/counter

        if is_prime(counter) and (counter > max_factor):
            max_factor = counter

    counter +=1

#################################
finish = time.time()

print(max_factor)
print(finish - start)


