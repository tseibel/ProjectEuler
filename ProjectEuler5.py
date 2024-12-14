# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import time
start = time.time()
################################

def is_divisible(number):
    counter = 2
    for counter in [19, 18, 17, 16, 15, 14, 12, 11]:
        if not number%counter == 0:
            return False
        
    return True

divisible = False
counter = 260

while divisible == False:
    if is_divisible(counter):
        divisible = True
        final_value = counter
    counter += 260 # because of 20 and 13

#################################
finish = time.time()

print(final_value)
print(finish - start)

