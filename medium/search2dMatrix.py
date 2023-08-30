# LeetCode Problem 74. Search a 2D Matrix
# Difficulty - Medium
# Author - Joshua Land
# url - "https://leetcode.com/problems/search-a-2d-matrix/description/"

"""
You are given an m x n integer matrix matrix with the following two properties:
    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of
    the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
"""

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        matrix_zero_type = type(matrix)
        
        # Start With Base Case.
        if matrix_zero_type == int:
            return target == matrix
        # trim it if its a list with one list.
        elif len(matrix) == 1 and matrix_zero_type == list:
            matrix = matrix[0]
            return self.searchMatrix(matrix, target)

        pivot = len(matrix) // 2
        
        # get the number if its 2d or not.
        if type(matrix[pivot]) == list:
            number = matrix[pivot][0]
        else: 
            number = matrix[pivot]

        # here is the comparison, then alter the list and recursion!
        if number == target:
            return True
        elif number < target:
            matrix = matrix[pivot:]
            return self.searchMatrix(matrix, target)
        elif number > target:
            matrix = matrix[:pivot]
            return self.searchMatrix(matrix, target)


# ********************** DRIVER CODE FOR leetCodeTester.py ********************
        # self.function_to_test = self.solution.searchMatrix # add the function name here
        
        # self.valid_input = [[[1,3,5,7],[10,11,16,20],[23,30,34,60]], [[1,3,5,7],[10,11,16,20],[23,30,34,60]], [[1]]] # this is an array of valid input
        # self.second_valid_input = [3, 13, 0]
        # self.multiple_inputs = True
        # self.expected_output = ['True', 'false', 'false']

# ********************** NOTES ************************************************    
    # My first thought is binary search
    # its just the first one i thought of that meets the O(log(m * n))
    # second thought, recursion.
    
    # Accepted Python3 52 ms 16.9 MB only beats 60%.. not as slick as i thought.
    
    # edit: I know now that recursion isnt best for this as its almost always slower.