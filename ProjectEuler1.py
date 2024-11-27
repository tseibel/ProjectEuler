#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000 

import time
start = time.time()
################################
count = 0
total = 0

while count <= 999:
    if count//3 == count/3:
        print(count, "three")
        total = total + count
    else:
        if count//5 == count/5:
            print(count, "five")
            total = total + count
    count = count + 1
#################################
finish = time.time()

print(total)
print(finish - start)

