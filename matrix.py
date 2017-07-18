"""
Functions for working with matrices.

Here we treat matrices as lists of lists with each inner list having the
same size representing a row of the matrix.

If A is a matrix, then A[i][j] is the element in the ith row and jth column.
"""

import validator as valid


def shape(matrix):
    """
    The matrix A has len(matrix) rows and len(matrix[0]) columns.

    Args:
        matrix (List): List of lists representing the matrix.

    Returns:
        A tuple of the format (rows, columns) of the matrix.

    Examples:
        >>> x = [[1, 2, 3],[1, 2, 3]]
        >>> shape(x)
        (2, 3)

        >>> y = [[1, 2, 3],[1, 2]]
        >>> shape(y)
        Traceback (most recent call last):
            ...
        IndexError: Each row must have the same number of columns.
    """
    valid_matrix, problems = valid.is_matrix(matrix)

    if not valid_matrix:
        raise IndexError(" ".join(problems))

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    return num_rows, num_cols


def get_row(matrix, i):
    """
    Get the ith row from a matrix.

    Args:
        matrix (List): List of lists representing the matrix.
        i (Int): The ith row to return as a vector.

    Returns:
        The requested vector from the matrix.

    Examples:
        >>> x = [[1, 2, 3], [4, 5, 6]]
        >>> get_row(x, 1)
        [4, 5, 6]

        >>> get_row(x, 3)
        Traceback (most recent call last):
            ...
        IndexError: This matrix only has 2 rows but row 3 was requested.

        >>> y = [[1, 2, 3],[1, 2]]
        >>> get_row(y, 0)
        Traceback (most recent call last):
            ...
        IndexError: Each row must have the same number of columns.
    """
    valid_matrix, problems = valid.is_matrix(matrix)

    if not valid_matrix:
        raise IndexError(" ".join(problems))

    num_rows, _ = shape(matrix)

    if i > num_rows:
        message = ('This matrix only has ' +
                   str(num_rows) +
                   ' rows but row ' +
                   str(i) +
                   ' was requested.')
        raise IndexError(message)

    return matrix[i]


def get_col(matrix, j):
    """
    Get the jth column from a matrix.

    Args:
        matrix (List): List of lists representing the matrix.
        j (Int): The jth column to return as a vector.

    Returns:
        The requested vector from the matrix.

    Examples:
        >>> x = [[1, 2, 3], [4, 5, 6]]
        >>> get_col(x, 1)
        [2, 5]

        >>> get_col(x, 4)
        Traceback (most recent call last):
            ...
        IndexError: This matrix only has 3 columns but column 4 was requested.

        >>> y = [[1, 2, 3],[1, 2]]
        >>> get_col(y, 0)
        Traceback (most recent call last):
            ...
        IndexError: Each row must have the same number of columns.
    """
    valid_matrix, problems = valid.is_matrix(matrix)

    if not valid_matrix:
        raise IndexError(" ".join(problems))

    _, num_cols = shape(matrix)

    if j > num_cols:
        message = ('This matrix only has ' +
                   str(num_cols) +
                   ' columns but column ' +
                   str(j) +
                   ' was requested.')
        raise IndexError(message)

    return [A_i[j] for A_i in matrix]


def make_matrix(num_rows, num_cols, entry_fn):
    """
    Create a matrix with num_rows rows and num_cols cols and populate the
    values of the matrix using entry_fn.

    Args:
        num_rows (Int): The number of rows in the output matrix.
        num_cols (Int): The number of columns in the output matrix.
        entry_fn (Function): A function to generate the values in the matrix.

    Returns:
        A matrix (List of Lists).

    Examples:
        >>> make_matrix(2, 2, lambda i, j: 1 if i ==j else 0)
        [[1, 0], [0, 1]]
    """
    new_matrix = [[entry_fn(i, j)
                   for j in range(num_cols)]
                  for i in range(num_rows)]

    valid_matrix, problems = valid.is_matrix(new_matrix)

    if not valid_matrix:
        raise IndexError(" ".join(problems))

    return new_matrix


def is_diagonal(i, j):
    """1's on the 'diagonal', 0's everywhere else"""
    return 1 if i == j else 0
