"""
    Module name :- solver
    Method(s) :- solver(n)
"""

def solver(n):
    """
    Find the sum of digit of 2^n.

    Args:-
        n(int) :- Power of 2.

    Return
        Sum of digits of 2^n.
    """
    product = 1
    total = 0

    for _ in range(1, n + 1):
        product = product * 2

    for digit in str(product):
        total += int(digit)

    return total


if __name__ == "__main__":
    print(f"solver(15) = {solver(15)}")
