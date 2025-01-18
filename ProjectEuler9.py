# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.

# Find the product abc. 


import time
import math

start = time.time()
##########################################

sum = 1000

for x in range(1, sum // 3):
    for y in range(x+1, (sum - x) // 2):
        z = sum - x - y
        if x**2 + y**2 == z**2:
            print(f"{x}, {y}, {z}")
            answer = x*y*z

##########################################
finish = time.time()

print(answer)
print(finish - start)
