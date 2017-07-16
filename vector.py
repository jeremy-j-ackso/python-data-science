"""
This module provides the necessary functionality for working with vectors.
"""
import math
import validator as valid

from functools import reduce


def vector_add(v1, v2):
    """
    Adds Corresponding elements in two vectors (lists) of the same length.

    Args:
        v1, v2 (List): Lists of the same length representing the vectors.

    Returns:
        A new vector of the same length as v1 and v2, where the corresponding
        elements have been added to each other.

    Examples:
        >>> x = [1, 2, 3]
        >>> y = [1, 2, 3]
        >>> vector_add(x, y)
        [2, 4, 6]

        >>> z = [1, 3]
        >>> vector_add(x, z)
        Traceback (most recent call last):
            ...
        IndexError: Vectors must be the same length

        >>> w = [1,2,[1,2]]
        >>> vector_add(x, w)
        Traceback (most recent call last):
            ...
        IndexError: One of the vectors passed is not a valid vector
    """
    if not (valid.is_vector(v1) and valid.is_vector(v2)):
        raise IndexError("One of the vectors passed is not a valid vector")

    if len(v1) != len(v2):
        raise IndexError('Vectors must be the same length')

    return [v1_i + v2_i
            for v1_i, v2_i in zip(v1, v2)]


def vector_subtract(v1, v2):
    """
    Subtracts Corresponding elements in two vectors (lists) of the same length.

    Args:
        v1, v2 (List): Lists of the same length representing the vectors.

    Returns:
        A new vector of the same length as v1 and v2, where the corresponding
        elements have been subtracted to each other.

    Examples:
        >>> w = [3, 2, 1]
        >>> x = [1, 2, 3]
        >>> vector_subtract(w, x)
        [2, 0, -2]

        >>> y = [1, 2, 3]
        >>> vector_subtract(x, y)
        [0, 0, 0]

        >>> z = [1, 3]
        >>> vector_subtract(x, z)
        Traceback (most recent call last):
            ...
        IndexError: Vectors must be the same length

        >>> e = [1,2,[1,2]]
        >>> vector_subtract(x, e)
        Traceback (most recent call last):
            ...
        IndexError: One of the vectors passed is not a valid vector
    """
    if not (valid.is_vector(v1) and valid.is_vector(v2)):
        raise IndexError("One of the vectors passed is not a valid vector")

    if len(v1) != len(v2):
        raise IndexError('Vectors must be the same length')

    return [v1_i - v2_i
            for v1_i, v2_i in zip(v1, v2)]


def vector_sum(vectors):
    """
    Sum Corresponding elements in all vectors (lists) of the same length.

    Args:
        vectors (List): Lists of the same length representing the vectors.

    Returns:
        A new vector of the same length as all of the vectors, where the
        corresponding elements have been summed.

    Examples:
        >>> w = [1, 2, 3]
        >>> x = [1, 2, 3]
        >>> y = [1, 2, 3]
        >>> myVecs = [w, x, y]
        >>> vector_sum(myVecs)
        [3, 6, 9]

        >>> z = [1, 3]
        >>> myVecs = [w, x, y, z]
        >>> vector_sum(myVecs)
        Traceback (most recent call last):
            ...
        IndexError: Vectors must be the same length

        >>> e = [1, 2, [1, 2]]
        >>> vector_sum([w, x, y, e])
        Traceback (most recent call last):
            ...
        IndexError: One of the vectors passed is not a valid vector
    """
    if not all(valid.is_vector(v) for v in vectors):
        raise IndexError("One of the vectors passed is not a valid vector")

    lengthToTest = len(vectors[0])
    if any(len(v) != lengthToTest for v in vectors[1:]):
        raise IndexError('Vectors must be the same length')

    return reduce(vector_add, vectors)


def scalar_multiply(v, sc):
    """
    Multiply a vector by a scalar.

    Args:
        v (List): List representing the vector.
        sc (int or float): Scalar to multiply by.

    Returns:
        A new vector of the same length as all of the vectors, where the
        corresponding elements have been summed.

    Examples:
        >>> scalar_multiply([1, 2, 3], 1)
        [1, 2, 3]

        >>> scalar_multiply([1, 2, 3], 2)
        [2, 4, 6]

        >>> scalar_multiply([1, 2, [1, 2]], 1)
        Traceback (most recent call last):
            ...
        IndexError: The vector passed is not a valid vector
    """
    if not valid.is_vector(v):
        raise IndexError("The vector passed is not a valid vector")

    return [i * sc for i in v]


def vector_mean(vectors):
    """
    Compute the vector whose ith element is the mean of the ith elements of
    the input vectors

    Args:
        vectors (List): List containing all of the vectors to be computed
        against.

    Returns:
        A new vector of the same length as all of the vectors, where the
        corresponding elements have had a mean calculated on them.

    Examples:
        >>> myVecs = [ [1, 2, 3], [1, 2, 3], [1, 2, 3] ]
        >>> vector_mean(myVecs)
        [1.0, 2.0, 3.0]

        >>> myVecs = [ [1, 2, 3], [2, 2, 2], [3, 2, 1] ]
        >>> vector_mean(myVecs)
        [2.0, 2.0, 2.0]

        >>> myVecs = [ [1, 2, 3], [2, 2, 2], [2, 1] ]
        >>> vector_mean(myVecs)
        Traceback (most recent call last):
            ...
        IndexError: Vectors must be the same length

        >>> myVecs = [ [1, 2, 3], [2, 2, 2], [2, 1, [1, 2] ] ]
        >>> vector_mean(myVecs)
        Traceback (most recent call last):
            ...
        IndexError: One of the vectors passed is not a valid vector
    """
    if not all(valid.is_vector(v) for v in vectors):
        raise IndexError("One of the vectors passed is not a valid vector")

    n = len(vectors)
    return scalar_multiply(vector_sum(vectors), 1/n)


def dot(v1, v2):
    """
    Compute the dot product of two vectors.

    Args:
        v1, v2 (List): The vectors for which a dot product will be computed.
            Must be the same length.

    Returns:
        A scalar of the dot product of the two vectors.

    Examples:
        >>> w = [1, 2, 3]
        >>> x = [1, 2, 3]
        >>> dot(w, x)
        14

        >>> z = [1, 2]
        >>> dot(x, z)
        Traceback (most recent call last):
            ...
        IndexError: Vectors must be the same length

        >>> e = [1, 2, [1, 2]]
        >>> dot(x, e)
        Traceback (most recent call last):
            ...
        IndexError: One of the vectors passed is not a valid vector
    """
    if not (valid.is_vector(v1) and valid.is_vector(v2)):
        raise IndexError("One of the vectors passed is not a valid vector")

    if len(v1) != len(v2):
        raise IndexError('Vectors must be the same length')

    return sum(v1_i * v2_i
               for v1_i, v2_i in zip(v1, v2))


def sum_of_squares(v):
    """
    Compute the sum of squares of for a vector

    Args:
        v (List): The vector for which the sum of squares should be calculated.

    Returns:
        A scalar of the sum of squares of the vector.

    Examples:
        >>> x = [1, 2, 3]
        >>> sum_of_squares(x)
        14

        >>> e = [1, 2, [1, 2]]
        >>> sum_of_squares(e)
        Traceback (most recent call last):
            ...
        IndexError: The vector passed is not a valid vector
    """
    if not valid.is_vector(v):
        raise IndexError("The vector passed is not a valid vector")

    return dot(v, v)


def magnitude(v):
    """
    Compute the magnitude of a vector

    Args:
        v (List): The vector for which the magnitude should be calculated.

    Returns:
        A scalar of the magnitude of the vector.

    Examples:
        >>> x = [1, 2, 3]
        >>> magnitude(x)
        3.7416573867739413

        >>> e = [1, 2, [1, 2]]
        >>> magnitude(e)
        Traceback (most recent call last):
            ...
        IndexError: The vector passed is not a valid vector
    """
    if not valid.is_vector(v):
        raise IndexError("The vector passed is not a valid vector")

    return math.sqrt(sum_of_squares(v))


def squared_distance(v1, v2):
    """
    Compute the squared distance between two vectors.

    Args:
        v1, v2 (List): The vectors for which a squared distance will be
        computed.

    Returns:
        A scalar of the squared distance between the vectors.

    Examples:
        >>> x = [1, 2, 3]
        >>> y = [3, 2, 1]
        >>> squared_distance(x, y)
        8

        >>> e = [1,2,[1,2]]
        >>> squared_distance(x, e)
        Traceback (most recent call last):
            ...
        IndexError: One of the vectors passed is not a valid vector
    """
    if not (valid.is_vector(v1) and valid.is_vector(v2)):
        raise IndexError("One of the vectors passed is not a valid vector")

    return sum_of_squares(vector_subtract(v1, v2))


def distance(v1, v2):
    """
    Compute the distance between two vectors.

    Args:
        v1, v2 (List): The vectors for which a distance will be computed.

    Returns:
        A scalar of the distance between the vectors.

    Examples:
        >>> x = [1, 2, 3]
        >>> y = [3, 2, 1]
        >>> distance(x, y)
        2.8284271247461903

        >>> e = [1, 2, [1, 2]]
        >>> distance(x, e)
        Traceback (most recent call last):
            ...
        IndexError: One of the vectors passed is not a valid vector
    """
    if not (valid.is_vector(v1) and valid.is_vector(v2)):
        raise IndexError("One of the vectors passed is not a valid vector")

    return magnitude(vector_subtract(v1, v2))
