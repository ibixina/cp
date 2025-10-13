import math
import statistics
import itertools

def mean(numbers):
    return statistics.mean(numbers)



def squared_sum(numbers):
    return sum(x**2 for x in numbers)


n, k = map(int, input().split())

numbers = []

for _ in range(n):
    numbers.append(int(input()))

combinations = itertools.combinations(numbers, k)

min_bad = math.inf


for combination in combinations:
    m= mean(combination)
    x = [(m - x) ** 2 for x in combination]
    sum_x = sum(x)
    min_bad = min(min_bad, sum_x)

print(min_bad)
