"""
This module contains statistics functions.
"""

from collections import Counter
import math

from vector import sum_of_squares, dot
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


def data_range(vector):
    """
    Returns max(vector) - min(vector). Only works for vectors containing
    Int and Float values. Errors on character vectors.

    Args:
        vector (List): A vector to calculate against.

    Returns:
        A scalar value of the same type as the vector.

    Examples:
        >>> w = [1, 2, 3]
        >>> data_range(w)
        2

        >>> x = [1.0, 2.0, 3.0]
        >>> data_range(x)
        2.0

        >>> y = ['a', 'b', 'c']
        >>> data_range(y) # doctest: +NORMALIZE_WHITESPACE
        Traceback (most recent call last):
            ...
        TypeError: The vector passed must contains either Int or Float values.

        >>> z = [1, 2, [1, 2]]
        >>> data_range(z)
        Traceback (most recent call last):
            ...
        IndexError: The vector passed is not a valid vector
    """
    if not (valid.is_vector(vector) and valid.is_vector(vector)):
        raise IndexError("The vector passed is not a valid vector")

    if any(isinstance(i, str) for i in vector):
        message = ("The vector passed must contains either " +
                   "Int or Float values.")
        raise TypeError(message)

    return max(vector) - min(vector)


def de_mean(vector):
    """
    Translate the vector by subtracting its mean, so the result has mean=0.

    Args:
        vector (List): a valid vector

    Returns:
        A vector (List), centered on 0.

    Examples:
        >>> x = [1, 2, 3]
        >>> de_mean(x)
        [-1.0, 0.0, 1.0]

        >>> y = ['a', 'b', 'c']
        >>> de_mean(y) # doctest: +NORMALIZE_WHITESPACE
        Traceback (most recent call last):
            ...
        TypeError: The vector passed must contains either Int or Float values.

        >>> z = [1, 2, [1, 2]]
        >>> de_mean(z)
        Traceback (most recent call last):
            ...
        IndexError: The vector passed is not a valid vector
    """
    if not (valid.is_vector(vector) and valid.is_vector(vector)):
        raise IndexError("The vector passed is not a valid vector")

    if any(isinstance(i, str) for i in vector):
        message = ("The vector passed must contains either " +
                   "Int or Float values.")
        raise TypeError(message)

    x_bar = mean(vector)

    return [x_i - x_bar for x_i in vector]


def variance(vector):
    """
    Calculate the variance of a vector with length >= 2.

    Args:
        vector (List): A vector containing 2 or more Int or Float values.

    Returns:
        A scalar representing the variance.

    Examples:
        >>> x = [1, 2, 3]
        >>> variance(x)
        1.0

        >>> y = ['a', 'b', 'c']
        >>> variance(y) # doctest: +NORMALIZE_WHITESPACE
        Traceback (most recent call last):
            ...
        TypeError: The vector passed must contains either Int or Float values.

        >>> z = [1, 2, [1, 2]]
        >>> variance(z)
        Traceback (most recent call last):
            ...
        IndexError: The vector passed is not a valid vector

        >>> zz = [1]
        >>> variance(zz)
        Traceback (most recent call last):
            ...
        IndexError: The vector must contain at least two values
    """
    if not (valid.is_vector(vector) and valid.is_vector(vector)):
        raise IndexError("The vector passed is not a valid vector")

    if any(isinstance(i, str) for i in vector):
        message = ("The vector passed must contains either " +
                   "Int or Float values.")
        raise TypeError(message)

    if len(vector) < 2:
        raise IndexError("The vector must contain at least two values")

    num_elements = len(vector)

    deviations = de_mean(vector)

    return sum_of_squares(deviations) / (num_elements - 1)


def standard_deviation(vector):
    """
    Computes the standard deviation of a vector.

    Args:
        vector (List): A vector.

    Returns:
        A scalar value representing the standard deviation.

    Examples:
        >>> x = [1, 2, 3]
        >>> standard_deviation(x)
        1.0

        >>> y = ['a', 'b', 'c']
        >>> standard_deviation(y) # doctest: +NORMALIZE_WHITESPACE
        Traceback (most recent call last):
            ...
        TypeError: The vector passed must contains either Int or Float values.

        >>> z = [1, 2, [1, 2]]
        >>> standard_deviation(z)
        Traceback (most recent call last):
            ...
        IndexError: The vector passed is not a valid vector

        >>> zz = [1]
        >>> standard_deviation(zz)
        Traceback (most recent call last):
            ...
        IndexError: The vector must contain at least two values
    """
    if not (valid.is_vector(vector) and valid.is_vector(vector)):
        raise IndexError("The vector passed is not a valid vector")

    if any(isinstance(i, str) for i in vector):
        message = ("The vector passed must contains either " +
                   "Int or Float values.")
        raise TypeError(message)

    if len(vector) < 2:
        raise IndexError("The vector must contain at least two values")

    return math.sqrt(variance(vector))


def interquartile_range(vector):
    """
    Calculates the difference between the 75th and 25th percentile.

    Args:
        vector (List): A numeric vector.

    Returns:
        A scalar value representing the interquartile range.

    Examples:
        >>> x = [*range(10)]
        >>> interquartile_range(x)
        5

        >>> y = ['a', 'b', 'c']
        >>> interquartile_range(y) # doctest: +NORMALIZE_WHITESPACE
        Traceback (most recent call last):
            ...
        TypeError: The vector passed must contains either Int or Float values.

        >>> z = [1, 2, [1, 2]]
        >>> interquartile_range(z)
        Traceback (most recent call last):
            ...
        IndexError: The vector passed is not a valid vector
    """
    if not (valid.is_vector(vector) and valid.is_vector(vector)):
        raise IndexError("The vector passed is not a valid vector")

    if any(isinstance(i, str) for i in vector):
        message = ("The vector passed must contains either " +
                   "Int or Float values.")
        raise TypeError(message)

    return quantile(vector, 0.75) - quantile(vector, 0.25)


def covariance(v_1, v_2):
    """
    Calculates the covariance of two vectors.

    Args:
        v_1, v_2 (List): List vectors of the same length.

    Returns:
        A scalar value of the covariance.

    Examples:
        >>> x = [1, 2, 3]
        >>> y = [3, 2, 1]
        >>> covariance(x, y)
        -1.0

        >>> z = [1, 2]
        >>> covariance(x, z)
        Traceback (most recent call last):
            ...
        IndexError: The two vectors must be the same length.

        >>> zz = ['a', 'b', 'c']
        >>> covariance(x, zz) # doctest: +NORMALIZE_WHITESPACE
        Traceback (most recent call last):
            ...
        TypeError: The vector passed must contains either Int or Float values.

        >>> zzz = [1, 2, [1, 2]]
        >>> covariance(x, zzz)
        Traceback (most recent call last):
            ...
        IndexError: The vector passed is not a valid vector
    """
    if not len(v_1) == len(v_2):
        raise IndexError("The two vectors must be the same length.")

    if not (valid.is_vector(v_1) and valid.is_vector(v_2)):
        raise IndexError("The vector passed is not a valid vector")

    chk = v_1.copy()
    chk.extend(v_2)
    if any(isinstance(i, str) for i in chk):
        message = ("The vector passed must contains either " +
                   "Int or Float values.")
        raise TypeError(message)

    num_elements = len(v_1)

    return dot(de_mean(v_1), de_mean(v_2)) / (num_elements - 1)


def correlation(v_1, v_2):
    """
    Calculates the correlation between two vectors.

    Args:
        v_1, v_2 (List): List vectors of the same length.

    Returns:
        A scalar value representing the correlation.

    Examples:
        >>> x = [1, 2, 3]
        >>> y = [3, 2, 1]
        >>> correlation(x, y)
        -1.0

        >>> z = [1, 2]
        >>> correlation(x, z)
        Traceback (most recent call last):
            ...
        IndexError: The two vectors must be the same length.

        >>> zz = ['a', 'b', 'c']
        >>> correlation(x, zz) # doctest: +NORMALIZE_WHITESPACE
        Traceback (most recent call last):
            ...
        TypeError: The vector passed must contains either Int or Float values.

        >>> zzz = [1, 2, [1, 2]]
        >>> correlation(x, zzz)
        Traceback (most recent call last):
            ...
        IndexError: The vector passed is not a valid vector
    """
    if not len(v_1) == len(v_2):
        raise IndexError("The two vectors must be the same length.")

    if not (valid.is_vector(v_1) and valid.is_vector(v_2)):
        raise IndexError("The vector passed is not a valid vector")

    chk = v_1.copy()
    chk.extend(v_2)
    if any(isinstance(i, str) for i in chk):
        message = ("The vector passed must contains either " +
                   "Int or Float values.")
        raise TypeError(message)

    sd_v_1 = standard_deviation(v_1)
    sd_v_2 = standard_deviation(v_2)

    if sd_v_1 > 0 and sd_v_2 > 0:
        return covariance(v_1, v_2) / sd_v_1 / sd_v_2
    else:
        return 0
