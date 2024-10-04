#!/usr/bin/python3
'''
implimentation of the Pascal's Triangle.
'''


def pascal_triangle(n):
    '''
    Returns a list of lists representing the Pascal's triangle of n.
    '''
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1] + [prev_row[j] + prev_row[j + 1] for j in range(
              len(prev_row) - 1)] + [1]
        triangle.append(row)

    return triangle
