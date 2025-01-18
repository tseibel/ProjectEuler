# In the 20 x 20 grid below, four numbers along a diagonal line have been marked in red.
# The product of these numbers is 26 x 63 x 78 x 14 = 1788696

# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20 x 20 grid?

import time
import math

from params import grid_11

start = time.time()
##########################################

grid = [int(x) for x in grid_11.split()]

def left_diag_product(grid):
    max_product = 0
    max_step_values = None
    for x in range(0, 340, 20): # Row
        for y in range(19, 2, -1): # Column
            step_values = []
            steps = [x + (i * 19) + y for i in range(0, 4, 1)]
            product = 1
            for step in steps:
                product *= grid[step]
                step_values.append(grid[step])

            if product > max_product:
                max_product = product
                max_step_values = step_values

    return max_product, max_step_values

def right_diag_product(grid):
    max_product = 0
    max_step_values = None
    for x in range(0, 340, 20): # Row
        for y in range(0, 17): # Column
            step_values = []
            steps = [x + (i * 21) + y for i in range(0, 4)]
            product = 1
            for step in steps:
                product *= grid[step]
                step_values.append(grid[step])
            
            if product > max_product:
                max_product = product
                max_step_values = step_values

    return max_product, max_step_values

def vertical_product(grid):
    max_product = 0
    max_step_values = None
    for x in range(0,20): # Column
        for y in range(0, 17): # Start Rows
            step_values = []
            steps = [x + (20 * i) for i in range(y, y+4)]
            product = 1
            for step in steps:
                product *= grid[step]
                step_values.append(grid[step])

            if product > max_product:
                max_product = product
                max_step_values = step_values

    return max_product, max_step_values

def horizontal_product(grid):
    max_product = 0
    max_step_values = None
    for x in range(0, 400, 20):
        for y in range(0, 17):
            step_values = []
            steps = [i for i in range(y+x, y+x+4)]
            product = 1
            for step in steps:
                product *= grid[step]
                step_values.append(grid[step])

            if product > max_product:
                max_product = product
                max_step_values = step_values

    return max_product, max_step_values

print(horizontal_product(grid))
print(vertical_product(grid))
print(right_diag_product(grid))
print(left_diag_product(grid))



##########################################
finish = time.time()

#print(answer)
print(finish - start)
