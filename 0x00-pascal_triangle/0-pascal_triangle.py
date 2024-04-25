#!/usr/bin/python3
"""Module of Pascal's Triangle"""

def pascal_triangle(n):
    """
    function that returns a list of lists of integers representing
    the Pascal triangle of n.
    """
    if n <= 0:
        return []

    pascal_list = []
    triangle = []

    for i in range(n):
        row = [1,]
        if triangle:
            for j in range(len(triangle)):
                if j != 0:
                    row.append(triangle[j - 1] + triangle[j])
            row.append(1)
        triangle = row
        pascal_list.append(row)

    return pascal_list

# result = pascal_triangle(7)
# for row in result:
#     print(row)
