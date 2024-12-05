import time
import numpy as np

puzzle_input = 34000000

start = time.time()

# Part A
houses = np.zeros((puzzle_input//10,), dtype=int)
for i in range(1, puzzle_input//10):
    number = i * 10
    houses[i::i] += number

it = np.nditer(houses, flags=['f_index'])
while not it.finished:
    if it[0] >= puzzle_input:
        print(it.index)
        break
    it.iternext()

# Part B
houses = np.zeros((puzzle_input//10,), dtype=int)
for i in range(1, puzzle_input//10):
    number = i * 11
    houses[i:50*i+1:i] += number

it = np.nditer(houses, flags=['f_index'])
while not it.finished:
    if it[0] >= puzzle_input:
        print(it.index)
        break
    it.iternext()

end = time.time()
print("Time: " + str(end-start))
