"""
Simulates the total payout of the casino and player over many turns.
"""

from random import randint, sample

TRIALS = 1000000

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

payouts = {
    4: 1000,
    5: 500,
    6: 500,
    7: 100,
    8: 100,
    9: 25,
    10: 5,
    11: 5,
    12: 5,
    13: 1,
    14: 0,
    15: 1,
    16: 5,
    17: 5,
    18: 5,
    19: 25,
    20: 100,
    21: 100,
    22: 500,
    23: 500,
    24: 1000
}

casino_earnings = []
player_earnings = []

for i in range(TRIALS):
    payout = payouts[sum(sample(board, 4))]
    casino_earnings.append(10 - payout)
    player_earnings.append(payout - 10)    

total_casino_earnings = sum(casino_earnings)
total_player_earnings = sum(player_earnings)
average_casino_earnings = total_casino_earnings / len(casino_earnings)
average_player_earnings = total_player_earnings / len(player_earnings)
print(f'Total Casino Earnings: {total_casino_earnings}, Total Player Earnings: {total_player_earnings}')
print(f'Average Casino Earnings: {average_casino_earnings}, Average Player Earnings: {average_player_earnings}')