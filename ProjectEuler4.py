# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 X 99

# Find the largest palindrome made from the product of two 3-digit numbers.

import time
start = time.time()
################################

def is_pal(number):
    number = str(number)
    digit = 0
    while digit < len(number) / 2:
        if number[digit] != number[-(digit+1)]:
            return False
        digit += 1
    
    return True

largest_pal = 0

for x in range(999, 99, -1):
    for y in range(x, 99, -1):
        if is_pal(x*y) and (x*y > largest_pal):
            largest_pal = x*y
            print(largest_pal)
            
#################################
finish = time.time()


print(largest_pal)
print(finish - start)

