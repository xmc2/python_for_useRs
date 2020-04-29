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
    # we will begin our search at the last row and first column
    a, b = matrix.shape[0] - 1, 0

    # x will track our matrix seach elements, saves a little
    # typing as well
    x = False

    # we will continue to search until we find the number
    while x != number:

    # updating x at the coordinates a,b
        x = matrix[a,b]

    # If the the matrix entry is less than the number we are
    # seeking, move one column to the right (increase b by 1)
        if x < number:
            b += 1

    # If the the matrix entry is greater than the number we are
    # seeking, move one row up (decrease a by 1)
        elif x > number:
            a -= 1

    # If we have identified the coordinates where our number is
    # loacted, print the number and end the loop
        elif x == number:
            print("Number Found at (", a+1, ",", b+1, ")")
            # loop ends here



###
### Example below:
###

import numpy as np

mat = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [65, 74, 76, 100]])

find_number(mat, 76)
