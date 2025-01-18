# The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ...+ 10 ^2 = 385
# The square of the sum of the first ten natural numbers is, (1 + 2 +...+ 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


import time

start = time.time()
##########################################
def sum_of_squares(x):
    if x == 0:
        return 0
    else:
        return sum_of_squares(x - 1) + (x * x) 

def square_of_sums(x):
    sum = 0
    for x in range(1,x+1):
        sum += x
    
    return sum * sum

answer = square_of_sums(100) - sum_of_squares(100)
##########################################
finish = time.time()

print(answer)
print(finish - start)
