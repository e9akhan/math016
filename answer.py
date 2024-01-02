"""
    Module name :- answer
    Method(s) :- answer()
"""

from solver import solver


def answer():
    """
    Find the sum of digit of 2^1000.

    Return
        Sum of digits of 2^1000.
    """
    return solver(1000)


if __name__ == "__main__":
    print(f"answer() = {answer()}")
