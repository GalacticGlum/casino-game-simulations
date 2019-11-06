"""
Calculuates the probability that a given sum occurs using an ordinary generating function.
"""

import sympy
from sympy import poly, srepr
from sympy.abc import x, y

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

# Compute the generating function
generating_function = 1
for k in board:
    generating_function *= poly(1 + x**k * y)

generating_function = generating_function.as_expr()

# Parse terms and map into data structure
# The coefficient of the x^k * y^n term as a tuple map.
coefficients = {}
for term in generating_function.as_ordered_terms():
    xpair = term.as_coeff_exponent(x)
    ypair = xpair[0].as_coeff_exponent(y)

    x_exponent = int(xpair[1])
    y_exponent = int(ypair[1])
    coefficient = int(ypair[0])

    coefficients[(x_exponent, y_exponent)] = coefficient

frequency = {}
# Calculate the frequency for rolling all sums (k in [4, 24]) with 4 (n) marbles
for k in range(4, 25):
    frequency[k] = coefficients[(k, 4)]

total = sum(frequency.values())
for key in sorted(frequency.keys()):
    print('{}: {} ({})'.format(key, frequency[key], frequency[key] / total))
