"""
This module contains statistics functions.
"""


def mean(vector):
    """
    Return the simple arithmatic mean of a vector.

    Args:
        x (List): A list vector containing the values to calculate against.

    Returns:
        A scalar Float value representing the mean of the values.

    Examples:
        >>> x = [2,2,2]
        >>> mean(x)
        2

        >>> y = [1,2,3]
        >>> mean(y)
        2

        >>> z = [1, 2, 3, [1, 2]]
        >>> mean(z)
        Traceback (most recent call last):
            ...
        IndexError: Vectors must be the same length
    """
    return sum(vector) / len(vector)
