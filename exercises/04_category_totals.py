"""Exercise 4: lists, loops, and functions.

Add another category and amount. Then change the function so it returns both
the total and the average.
"""

amounts = [12.5, 8.0, 15.25, 10.0]


def total(values):
    result = 0
    for value in values:
        result += value
    return result


print(f"Total: {total(amounts):.2f}")
