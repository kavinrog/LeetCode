def CountNegativeNumberUnsorted(matrix):
    """
    Count the number of negative number in a 2D Matrix
    :param matrix: List of List of integers
    :return: Integer representing the number of negative numbers
    """
    count = 0
    if not matrix or not matrix[0]:
        return 0
    for row in matrix:
        for val in row:
            if val < 0:
                count += 1
    return count 

# Test the function
if __name__ == "__main__":
    matrix = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    print(CountNegativeNumberUnsorted(matrix))  # Output: 8
    
    matrix = [[5, 3, 2], [4, 0, -1], [-2, -3, -4]]
    print(CountNegativeNumberUnsorted(matrix))  # Output: 5
    
    matrix = [[-1]]
    print(CountNegativeNumberUnsorted(matrix))  # Output: 1
