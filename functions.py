import math

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