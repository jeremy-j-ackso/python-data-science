"""
This module contains statistics functions.
"""

from collections import Counter
import validator as valid


def mean(vector):
    """
    Return the simple arithmatic mean of a vector.

    Args:
        vector (List): A list vector containing the values to calculate
        against.

    Returns:
        A scalar Float value representing the mean of the vector.

    Examples:
        >>> x = [2,2,2]
        >>> mean(x)
        2.0

        >>> y = [1,2,3]
        >>> mean(y)
        2.0

        >>> z = [1, 2, 3, [1, 2]]
        >>> mean(z)
        Traceback (most recent call last):
            ...
        IndexError: The vector passed is not a valid vector
    """
    if not (valid.is_vector(vector) and valid.is_vector(vector)):
        raise IndexError("The vector passed is not a valid vector")

    return sum(vector) / len(vector)


def median(vector):
    """
    Return the median (central value) of a vector.

    Args:
        vector (List): A list vector containing the values to calculate
        against.

    Returns:
        A scalar Float value representing the median of the vector.

    Examples:
        >>> w = [2, 2, 2]
        >>> median(w)
        2.0

        >>> x = [1, 2, 5]
        >>> median(x)
        2.0

        >>> y = [1, 2, 3, 4]
        >>> median(y)
        2.5

        >>> z = [1, 2, 3, [1, 2]]
        >>> median(z)
        Traceback (most recent call last):
            ...
        IndexError: The vector passed is not a valid vector
    """
    if not (valid.is_vector(vector) and valid.is_vector(vector)):
        raise IndexError("The vector passed is not a valid vector")

    elements = len(vector)
    sorted_vector = sorted(vector)
    midpoint = elements // 2

    if elements % 2 == 1:
        return float(sorted_vector[midpoint])
    else:
        low = midpoint - 1
        hih = midpoint
        return mean([sorted_vector[low], sorted_vector[hih]])


def quantile(vector, percentile):
    """
    Returns the desired percentile value of a vector.

    Args:
        vector (List): A list vector containing the values to calculate
        against.

        percentile (Float): A value of the sought percentile such that
        (0.0 < value < 1.0)

    Returns:
        A scalar value from the target vector, which represents the value less
        than which a certain percentile of the data lies.

    Examples:
        >>> x = [*range(10)]
        >>> quantile(x, 0.30)
        3

        >>> quantile(x, 0.90)
        9

        >>> quantile(x, 1.0) # doctest: +NORMALIZE_WHITESPACE
        Traceback (most recent call last):
            ...
        ValueError: The percentile must be a Float such that
        (0.0 < percentile < 1.0)

        >>> z = [1, 2, 3, [1, 2, 3]]
        >>> quantile(z, 0.50)
        Traceback (most recent call last):
            ...
        IndexError: The vector passed is not a valid vector
    """
    if not (percentile > 0.0 and percentile < 1.0):
        message = ('The percentile must be a Float such that ' +
                   '(0.0 < percentile < 1.0)')
        raise ValueError(message)

    if not (valid.is_vector(vector) and valid.is_vector(vector)):
        raise IndexError("The vector passed is not a valid vector")

    p_index = int(percentile * len(vector))

    return sorted(vector)[p_index]


def mode(vector):
    """
    Returns a list containing the most common value. Returns a list of
    len() > 1 in the case of ties.

    Args:
        vector (List): A list vector for which a mode is sought.

    Returns:
        A List containing one or more values which are the most frequent.

    Examples:
        >>> x = [1, 2, 3]
        >>> mode(x)
        [1, 2, 3]

        >>> y = [1, 2, 3, 2]
        >>> mode(y)
        [2]

        >>> z = [1, 2, [3, 4]]
        >>> mode(z)
        Traceback (most recent call last):
            ...
        IndexError: The vector passed is not a valid vector
    """
    if not (valid.is_vector(vector) and valid.is_vector(vector)):
        raise IndexError("The vector passed is not a valid vector")

    counts = Counter(vector)
    max_count = max(counts.values())

    return [x_i for x_i, count in counts.items()
            if count == max_count]
