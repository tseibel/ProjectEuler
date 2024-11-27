# The prime factors of 13915 are 5,7,13,29

# What is the largest prime factor of 600851475143

import time
import numpy as np

start = time.time()
##########################################

def is_prime(x):
    for i in range(2, x//2):
        if x%i == 0:
            return False
    
    return True

value = 600851475143 // 2 + 1

prime = False

while prime == False:
    if value%2 != 0:
        if value%5 != 0: 
            prime = is_prime(value)

    
    value -= 1

print(value + 1)
        
        
    



##########################################
finish = time.time()

print(finish-start)