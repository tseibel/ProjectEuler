# The sequence of triangle numbers is generated by adding the natural numbers. 
# So the 7th triangle number would be 1+2+3+4+5+6+7=28. 
# The first ten terms would be: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
# Let us list the factors of the first seven triangle numbers:
# 1 - 1
# 3 - 1,3
# 6 - 1, 3, 6
# 10 - 1, 10
# 15 - 1, 3, 5, 15
# 21 - 1, 3, 7, 21
# 28 - 1, 2, 4, 7, 24, 28
# 36
# 45
# 55

# We can see that 28 is the first triangle number to have over five divisors.

#What is the value of the first triangle number to have over five hundred divisors?

import time
import math

from functions import count_divisors,

start = time.time()
################################

max_divisors = 0
index = 2
current_number = 1

while index == 2:



    #reverse_sieve(current_number)

    current_number += index
    index += 1

"""

while max_divisors < 501:
    if math.sqrt(current_number) > 250:
        divisors = count_divisors(current_number)
        if divisors > max_divisors:
            answer = current_number
            max_divisors = divisors

    current_number += index
    index += 1
"""

#################################
finish = time.time()

print(answer)
print(finish - start)

