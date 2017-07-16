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
        >>> x = [1,2,3]
        >>> isVector(x)
        True

        >>> y = [1,2,[1,2]]
        >>> isVector(y)
        False
    """
    return all((isinstance(i, str) or
                isinstance(i, int) or
                isinstance(i, float))
               for i in to_check)
