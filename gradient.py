"""
Functions for Gradient Descent
"""


def difference_quotient(f, x, h):
    """
    Calculates the difference quotient of a function, given a variable and
    the error term.

    Args:
        f (Function): A function of one variable.
        x (Float): The starting point for gradient descent.
        h (Float): The starting point to bring to zero.

    Returns:
        Float.

    Examples:

    """
    return (f(x + h) - f(x)) / h


def partial_difference_quotient(f, v, i, h):
    """
    Compute the ith partial difference quotient of f at v.
    """
    w = [v_j + (h if j == i else 0)
         for j, v_j in enumerate(v)]

    return (f(w) - f(v)) / h


def estimate_gradient(f, v, h=0.00001):
    """
    Estimate on the gradient.
    """
    return [partial_difference_quotient(f, v, i, h)
            for i, _ in enumerate(v)]


def step(v, direction, step_size):
    """
    move step_size in the direction from v
    """
    return [v_i + step_size * direction_i
            for v_i, direction_i in zip(v, direction)]


def sum_of_squares_gradient(v):
    """
    Calculate the sum of squres for the gradient.
    """
    return [2 * v_i for v_i in v]
