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


def seq(value):
    values = [value]

    while values[-1] >= value:#not in result_dict.keys():

        if is_even(values[-1]):
            values.append(values[-1] / 2)
        else:
            values.append(3 * values[-1] + 1)

    return values

x = seq(1000000)
print(x)

"""
value = 2
result_dict = {1:1}
while value < 5000:

    values = seq(value)

    dict = {values[i]: result_dict[values[-1]] + len(values) - i - 1 for i in range(len(values) - 1)}
    #print('############')
    #print(dict)
    result_dict = result_dict | dict

    #print(result_dict)
    value += 1

print(result_dict)
"""
#################################
finish = time.time()

#print(answer)
print(finish - start)