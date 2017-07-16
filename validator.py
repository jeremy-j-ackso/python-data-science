"""
This functions in this module perform validation to check that their inputs
of the needed types for this project.
"""


def is_vector(to_check):
    """
    Checks if the argument is a single-leveled list, meaning that all of its
    contents are one of three acceptable types: Int, Float, or String.

    Args:
        to_check (List): The list to check for vectorhood.

    Returns:
        Boolean.

    Examples:
        >>> w = [1.0, 2.0, 3.0]
        >>> is_vector(w)
        True

        >>> x = [1, 2, 3]
        >>> is_vector(x)
        True


        >>> y = ['a', 'b', 'c']
        >>> is_vector(y)
        True

        >>> z = [1, 2, [1, 2]]
        >>> is_vector(z)
        False
    """
    return all((isinstance(i, str) or
                isinstance(i, int) or
                isinstance(i, float))
               for i in to_check)


def is_matrix(to_check):
    """
    Checks if the argument is a valid matrix, meaning that each list within
    the list is of the same length and and a valid type (Int, Float, String).

    Args:
        to_check (List): The list of lists to check for matrixhood.

    Return:
        A tuple where the first element indicates if the argument is a valid
        matrix and the second is a (possibly empty) List of Strings containing
        the problem messages to raise in the body of the error message.

    Examples
        >>> w = [ [1, 2, 3], [3, 2, 1] ]
        >>> is_matrix(w)
        (True, [])

        >>> x = [ [1, 2, 3], ['a', 'b', 'c'] ]
        >>> is_matrix(x)
        (True, [])

        >>> y = [ [1, 2, 3], ['a', 'b', 'c'], [1.0, 2.0, 3.0] ]
        >>> is_matrix(y)
        (True, [])

        >>> z = [ [1, 2, 3], [3, 2] ]
        >>> is_matrix(z)
        (False, ['Each row must have the same number of columns.'])

        >>> zz = [ [1, 2, 3], [3, 2, [3, 2]] ]
        >>> is_matrix(zz)
        (False, ['One of the rows in the matrix is not a valid vector.'])


        >>> zzz = [ [1, 2, 3], [3, 2], [4, 5, [5, 4]] ]
        >>> is_matrix(zzz) # doctest: +NORMALIZE__WHITESPACE
        (False,
         ['One of the rows in the matrix is not a valid vector.',
          'Each row must have the same number of columns.'])
    """
    collector = []

    if not all(is_vector(i) for i in to_check):
        collector.append('One of the rows in the matrix is not ' +
                         'a valid vector.')

    num_cols = len(to_check[0])

    if any([len(a) != num_cols for a in to_check]):
        collector.append('Each row must have the same number of columns.')

    valid_matrix = bool(len(collector))

    return valid_matrix, collector
