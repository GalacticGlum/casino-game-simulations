"""
Multiple alternative methods to computing the theoretical probabilities of the casino game.

These methods are based on analysis and formulas rather than simply brute-forcing all possible
combinations and counting their frequency.
"""

import operator
from itertools import combinations
from functools import reduce
from math import factorial

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0
    
board = [
    4, 3, 2, 4, 1, 4, 2, 3, 4,
    3, 4, 5, 3, 6, 3, 5, 4, 3,
    4, 3, 2, 4, 1, 4, 2, 3, 4,
    3, 4, 5, 3, 6, 3, 5, 4, 3,
    4, 3, 2, 4, 1, 4, 2, 3, 4,
    3, 4, 5, 3, 6, 3, 5, 4, 3,
    4, 3, 2, 4, 1, 4, 2, 3, 4,
    3, 4, 5, 3, 6, 3, 5, 4, 3,
    4, 3, 2, 4, 1, 4, 2, 3, 4
]

point_frequency = {}
for i in range(1, 7):
    point_frequency[i] = board.count(i)
    print('{}: {}'.format(i, board.count(i)))

probability_distribution = {}
visited = set()

for outcome in combinations(board, 4):
    outcome_id = ''.join(str(v) for v in sorted(outcome))
    if outcome_id in visited: continue
    visited.add(outcome_id)
    
    value_sum = sum(outcome)
    if value_sum not in probability_distribution:
        probability_distribution[value_sum] = 0
    
    unique_values = set(outcome)
    probability = factorial(4) / prod(factorial(outcome.count(i)) for i in unique_values)    
    count = 0
    for value in unique_values:
        for i in range(outcome.count(value)):
            probability *= (point_frequency[value] - i) / (len(board) - count)
            count += 1

    probability_distribution[value_sum] += probability

print('----')

frequency = {}
for v in visited:
    value_sum = sum(int(i) for i in v)
    if value_sum not in frequency:
        frequency[value_sum] = 0

    frequency[value_sum] += prod(choose(point_frequency[int(i)], v.count(i)) for i in set(v))

total = choose(81, 4)
for key in sorted(frequency.keys()):
    print('{}: {} ({})'.format(key, frequency[key], frequency[key] / total))

print('----')

for key in sorted(probability_distribution.keys()):    
    print('{}: {}'.format(key, probability_distribution[key]))
