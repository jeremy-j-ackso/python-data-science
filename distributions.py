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


# The normmal cdf is the probability the variable is below a threshold.
normal_probability_below = normal_cdf


def normal_probability_above(lo, mu=0, sigma=1):
    """
    A random variable is above the threshold if it's not below the threshold.

    Args:
        lo (Int or Float): A random variable.
        mu (Int or Float): The mean of the distribution.
        sigma (Int or Float): The standard deviation of the distribution.

    Returns:
        Float

    Examples:
        >>> normal_probability_above(0.5, 0, 1)
        0.3085375387259869
    """
    return 1 - normal_cdf(lo, mu, sigma)


def normal_probability_between(lo, hi, mu=0, sigma=1):
    """
    A random variable is between if it's less than hi, but not less than lo.

    Args:
        lo (Int or Float): A random variable.
        hi (Int or Float): A random variable.
        mu (Int or Float): The mean of the distribution.
        sigma (Int or Float): The standard deviation of the distribution.

    Returns:
        Float

    Examples:
        >>> normal_probability_between(0.2, 0.3, 0, 1)
        0.15773925946598155
    """
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, hi, sigma)


def normal_probability_outside(lo, hi, mu=0, sigma=1):
    """
    A random variable is outside if it's not between.

    Args:
        lo (Int or Float): A random variable.
        hi (Int or Float): A random variable.
        mu (Int or Float): The mean of the distribution.
        sigma (Int or Float): The standard deviation of the distribution.

    Returns:
        Float

    Examples:
        >>> normal_probability_between(0.2, 0.3, 0, 1)
        0.15773925946598155
    """
    return 1 - normal_probability_between(lo, hi, mu, sigma)


def normal_upper_bound(probability, mu=0, sigma=1):
    """
    Returns the z for which P(Z <= z) = probability.

    Args:
        probability (Float): A probability to test against.
        mu (Int or Float): The mean of the distribution.
        sigma (Int or Float): The standard deviation of the distribution.

    Returns:
        Float

    Examples:
        >>> normal_upper_bound(0.95, 0, 1)
        1.6448497772216797
        >>> normal_upper_bound(0.1, 0, 1)
        -1.2815570831298828
    """
    return inverse_normal_cdf(probability, mu, sigma)


def normal_lower_bound(probability, mu=0, sigma=1):
    """
    Returns the z for which P(Z >= z) = probability.

    Args:
        probability (Float): A probability to test against.
        mu (Int or Float): The mean of the distribution.
        sigma (Int or Float): The standard deviation of the distribution.

    Returns:
        Float
        >>> normal_lower_bound(0.95, 0, 1)
        -1.6448497772216797

        >>> normal_lower_bound(0.1, 0, 1)
        1.2815570831298828
    """
    return inverse_normal_cdf(1 - probability, mu, sigma)


def normal_two_sided_bounds(probability, mu=0, sigma=1):
    """
    Returns the symmetric bounds about the mean that contain the
    specified probability.

    Args:
        probability (Float): A probability to test against.
        mu (Int or Float): The mean of the distribution.
        sigma (Int or Float): The standard deviation of the distribution.

    Returns:
        Tuple of Floats

    Examples:
        >>> normal_two_sided_bounds(0.95, 500.0, 15.811388300841896)
        (469.01026640487555, 530.9897335951244)
    """
    tail_probability = (1 - probability) / 2
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound


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


def normal_approximation_to_binomial(n, p):
    """
    Finds the mu and sigma for a corresponding to a Binmoial(n, p).

    Args:
        n (Int): The number of bernoulli trials to run.
        p (Float): The probability to test against.

    Returns:
        Tuple containing (mu, sigma).

    Examples:
        >>> normal_approximation_to_binomial(1, 0.5)
        (0.5, 0.5)

        >>> normal_approximation_to_binomial(1000, 0.5)
        (500.0, 15.811388300841896)
    """
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma


def B(alpha, beta):
    """
    A normalizing constant so that the total probability is 1.

    Args:
        alpha (Float): An alpha value for the Beta distribution.
        beta (Float): A beta value for the Beta distribution.

    Returns:
        Float. The probablity of the two values in the Beta distribution.

    Examples:
        >>> B(1, 1)
        1.0

        >>> B(10, 1)
        0.1

        >>> B(1, 10)
        0.1
    """
    return math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)


def beta_pdf(x, alpha, beta):
    """
    Returns the pdf of a beta distribution.

    Args:
        x (Float): A weight such that 0 <= x <= 1.
        alpha (Float): An alpha value for the Beta distribution.
        beta (Float): A beta value for the Beta distribution.

    Returns:
        Float. The pdf of the beta distribution for the given values.

    Examples:
        >>> beta_pdf(0.5, 1, 1)
        1.0

        >>> beta_pdf(1, 1, 1)
        0

        >>> beta_pdf(0, 1, 1)
        0
    """
    if x <= 0 or x >= 1:
        return 0

    return x ** (alpha - 1) * (1 - x) ** (beta - 1) / B(alpha, beta)
