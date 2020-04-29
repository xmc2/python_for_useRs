# Function: find_number()
#
# Description: This function finds the coordinates of a
# known element within a matrix.
#
# Parameters:
#     matrix: This is the ordered matrix to be searched,
#             provided as a two dimensional numpy array.
#     number: This is the element within the given
#             matrix to be found.

def find_number(matrix, number):
    # setting a,b (the matrix search coordinates) to 0,0
    # we will begin our search at the first row and first column
    a, b = 0,0

    # x will track our matrix seach elements, saves a little
    # typing as well
    x = False

    # we will continue to search until we find the number
    while x != number:

    # updating x at the coordinates a,b
        x = matrix[a,b]

    # If the the matrix entry is less than the number we are
    # seeking, move one row down (increase a by 1)
        if x < number:
            a += 1

    # If the the matrix entry is greater than the number we are
    # seeking, move one column to the right (increase b by 1)
        elif x > number:
            b += 1

    # If we have identified the coordinates where our number is
    # loacted, print the number and end the loop
        elif x == number:
            print("Number Found at (", a+1, ",", b+1, ")")
            # loop ends here



###
### Example below:
###

import numpy as np

mat = np.array([[4,3,2,1],
                [8,7,6,5],
                [12,11,10,9],
                [100,76,74,65]])

find_number(mat, 76)
