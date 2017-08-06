"""
Statistical Tests
"""


import distributions as d


def two_sided_p_value(x, mu=0, sigma=1):
    """
    Compute the two-sided probability of seeing a particular value x in the
    distribution.

    Args:
        x (Float): The value to check for presence in the distribution.
        mu (Float): The mean of the distribution to check against.
        sigma (Float): The standard deviation of the distribution to check
        against.

    Results:
        Float, the probability of observing the x value in the given
        distribution.

    Examples:
        >>> two_sided_p_value(529.5, 500, 15.811388300841896)
        0.06207721579598857
    """
    if x >= mu:
        return 2 * d.normal_probability_above(x, mu, sigma)
    else:
        return 2 * d.normal_probability_below(x, mu, sigma)


upper_p_value = d.normal_probability_above
lower_p_value = d.normal_probability_below
