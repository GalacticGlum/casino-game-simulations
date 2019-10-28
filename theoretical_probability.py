"""
Calculuates the probability that a given sum occurs.
"""

from itertools import combinations

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

event_outcomes = {}
for outcome in combinations(board, 4):
    value_sum = sum(outcome)
    if value_sum not in event_outcomes:
        event_outcomes[value_sum] = 0
    
    event_outcomes[value_sum] += 1

probability_distribution = {}
total_combinations = choose(len(board), 4)
for key in event_outcomes:
    probability_distribution[key] = event_outcomes[key] / total_combinations

for key in sorted(probability_distribution.keys()):
    print(f'{key}: {probability_distribution[key] * 100}% ({probability_distribution[key]})')