#The following iterative sequence is defined for the set of positive integers:

## (n/2 is even)
## (3n+1 is odd)

#Using the rule above and starting with 13, we generate the following sequence:

# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), 
# It is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

import time
import math

from functions import is_even

start = time.time()
################################

dict_values = {}
value = 999999

while value > 1:
    values = [value]

    while values[-1] != 1:
        if is_even(values[-1]):
            values.append(values[-1] / 2)
        else:
            values.append(3 * values[-1] + 1)

    result_dict = {values[i]: len(values) - i for i in range(len(values))}

    print(value)
    value -= 1

print(result_dict)

#################################
finish = time.time()

#print(answer)
print(finish - start)