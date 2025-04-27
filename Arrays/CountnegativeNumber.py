def CountNegativeNumberUnsorted(matrix):
    """
    Count the number of negative number in a 2D Matrix
    :param matrix: List of List of integers
    :return: Integer representing the number of negative numbers
    """
    count = 0
    if not matrix or matrix[0]:
        return 0
    for row in matrix:
        for val in row:
            if val < 0:
                count += 1
    return count 
