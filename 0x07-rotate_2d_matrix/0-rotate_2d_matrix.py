#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a given 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list[list]): The 2D matrix to be rotated.

    Returns:
        None: The function modifies the matrix in-place.

    """
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # Save the top element
            top = matrix[layer][i]
            # Move left element to top
            matrix[layer][i] = matrix[-i - 1][layer]
            # Move bottom element to left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]
            # Move right element to bottom
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]
            # Move top element to right
            matrix[i][-layer - 1] = top
