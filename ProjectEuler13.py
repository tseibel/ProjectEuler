# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

import time
import math

from params import value_13

start = time.time()
################################

values = [int(num) for num in value_13.split()]
answer = str(sum(values))[:10]

#################################
finish = time.time()

print(answer)
print(finish - start)

