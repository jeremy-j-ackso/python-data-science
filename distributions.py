"""
Generate different distributions.
"""

import math
import random

from matplotlib import pyplot as plt
from collections import Counter


def uniform_pdf(x):
    """
    The probability that a variable is in a uniform distribution between 0
    and 1.

    Args:
        x (Int or Float): The value to check as part of a uniform distribution.

    Returns:
        Boolean

    Examples:
        >>> uniform_pdf(0.5)
        1

        >>> uniform_pdf(1)
        0

        >>> uniform_pdf(2)
        0

        >>> uniform_pdf(-1)
        0
    """
    return 1 if x >= 0 and x < 1 else 0


def uniform_cdf(x):
    """
    The probability that a random variable is less than or equal to a certain
    value.

    Args:
        x (Int or Float): The value to check as part of a uniform distribution.

    Returns:
        Float

    Examples:
        >>> uniform_cdf(-0.0001)
        0

        >>> uniform_cdf(0)
        0

        >>> uniform_cdf(0.5)
        0.5

        >>> uniform_cdf(0.9)
        0.9
    """
    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1


def normal_pdf(x, mu=0, sigma=1):
    """
    Returns the probability of x being part of a normal distribution defined
    by its mean (mu) and standard devaition (sigma).

    Args:
        x (Int or Float): A random variable.
        mu (Int or Float): The mean of the distribution.
        sigma (Int or Float): The standard deviation of the distribution.

    Returns:
        Float

    Examples:
        >>> normal_pdf(0, 0, 1)
        0.3989422804014327

        >>> normal_pdf(0, 20, 1)
        5.520948362159764e-88
    """
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))


def normal_cdf(x, mu=0, sigma=1):
    """
    Returns the cumulative probability of x being part of a normal distribution
    defined by its mean (mu) and standard deviation (sigma).

    Args:
        x (Int or Float): A random variable.
        mu (Int or Float): The mean of the distribution.
        sigma (Int or Float): The standard deviation of the distribution.

    Returns:
        Float

    Examples:
        >>> normal_cdf(0, 0, 1)
        0.5

        >>> normal_cdf(0, 20, 1)
        0.0
    """
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """
    Return a value of the specified probablity from the specified normal
    distribution with the specified value of decimal precision.

    Args:
        x (Int or Float): A random variable.
        mu (Int or Float): The mean of the distribution.
        sigma (Int or Float): The standard deviation of the distribution.
        tolerance (Float): The decimal precision to return.

    Returns:
        Float

    Examples:
        >>> inverse_normal_cdf(0, 0, 1, 0.00001)
        -8.75

        >>> inverse_normal_cdf(0, 20, 1, 0.1)
        11.25
    """
    # if the distribution is not standard normal, translate it so that it is.
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z = -10.0
    hi_z = 10.0
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            low_z = mid_z
        elif mid_p > p:
            hi_z = mid_z
        else:
            break

    return mid_z


def bernoulli_trial(probability):
    """
    Returns an integer 1 or 0 indicative of whether or not an internal random
    value is less than the probability given as an argument.

    Args:
        probability (Float): The probability to test against.

    Returns:
        Integer value of either 1 or 0.

    Examples:
        >>> random.seed(0)
        >>> bernoulli_trial(0.9)
        1
        >>> bernoulli_trial(0.1)
        0
    """
    return 1 if random.random() < probability else 0


def binomial(n, p):
    """
    Returns the sum of n bernoulli trials for probability p.

    Args:
        n (Int): The number of bernoulli trials to run.
        p (Float): The probability to test against.

    Returns:
        Integer, the sum of all bernoulli trials.

    Examples:
        >>> random.seed(0)
        >>> binomial(20, 0.5)
        7
    """
    return sum(bernoulli_trial(p) for _ in range(n))


def make_hist(p, n, num_points):
    """
    Builds a histogram as a barchart in matplotlib.

    Args:
        p (Float): The probability to test against.
        n (Int): The variable to checck against.
        num_points (Int): The number of bernoulli trials to run.

    Returns:
        Displays a matplotlib graphic in a new window.
    """
    data = [binomial(n, p) for _ in range(num_points)]

    histogram = Counter(data)

    plt.bar([x - 0.4 for x in histogram.keys()],
            [v / num_points for v in histogram.values()],
            color='0.75')

    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))

    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma)
          for i in xs]
    plt.plot(xs, ys)
    plt.title("Binomial Distribution vs Normal Approximation")
    plt.show()
