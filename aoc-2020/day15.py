from timeit import default_timer as timer

start = timer()
lines = [line.strip() for line in open("input/15.txt")]

numbers = [int(x) for x in lines[0].split(",")]

D = [-1] * 30_000_000
for i, num in enumerate(numbers):
    D[num] = i

previous = numbers[-1]
end1 = None
for t in range(len(numbers), 30_000_000):
    if end1 is None and t == 2020:
        print(previous)
        end1 = timer()
    new_previous = 0 if D[previous] == -1 else t - 1 - D[previous]
    D[previous] = t - 1
    previous = new_previous

end2 = timer()
print(previous)
print(f'Time for part 1: {end1 - start} seconds')
print(f'Time for part 2: {end2 - start} seconds')
