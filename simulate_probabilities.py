"""
Simulates the probability that specific sum occurs.
"""

from random import randint, sample

TRIALS = 100000000

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

for trail in range(TRIALS):
    value_sum = sum(sample(board, 4))
    if value_sum not in event_outcomes:
        event_outcomes[value_sum] = 0

    event_outcomes[value_sum] += 1

probability_distribution = {}
for key in event_outcomes:
    probability_distribution[key] = event_outcomes[key] / TRIALS * 100
    
for key in sorted(probability_distribution.keys()):
    print(f'{key}: {probability_distribution[key]}') 
