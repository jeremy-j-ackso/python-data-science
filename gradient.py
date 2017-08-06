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


def safe(f):
    """
    Returns a new function that's the same as f, except that it outputs
    infinity whenever f produces an error
    """
    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return float('inf')
    return safe_f


def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    """
    Use gradient descent to find theta that minimizes the target function.
    """
    step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]

    theta = theta_0
    target_fn = safe(target_fn)
    value = target_fn(theta)

    while True:
        gradient = gradient_fn(theta)
        next_thetas = [step(theta, gradient, -step_size)
                       for step_size in step_sizes]
        next_theta = min(next_thetas, key=target_fn)
        next_value = target_fn(next_theta)

        if abs(value - next_value) < tolerance:
            return theta
        else:
            theta, value = next_theta, next_value


def negate(f):
    """
    Return a function that for any input x returns -f(x)
    """
    return lambda *args, **kwargs: -f(*args, **kwargs)


def negate_all(f):
    """
    The same when f returns a list of numbers
    """
    return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]


def maximize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    """
    Use gradient descent to find theta that maximizes the target function.
    """
    return minimize_batch(negate(target_fn),
                          negate_all(gradient_fn),
                          theta_0,
                          tolerance)
