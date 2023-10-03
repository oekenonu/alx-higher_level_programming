#!/usr/bin/python3

""" Function that divides all elements of a matrix """

def matrix_divided(matrix, div):
    """
        function divides all elements of a matrix

    Args:
        matrix (list): A list of lists of type int or float
        div (int|float): The divisor of the matrix

    Raises:
        TypeError: If matrix is not a list of lists of integers or float
        TypeError: If matrix row is not same size
        TypeError: Id div is not of type int or float
        ZeroDivisionError: If div equals 0

    Returns:
        A new matrix that has been divided by div
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    for element in row:
        if not isinstance(element, (int, float)):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num/div, 2) for num in row] for row in matrix]
