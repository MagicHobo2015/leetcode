import curses
from curses import panel



def main():
    # test = [[x for x in range(1, 10)],
    #         [x for x in range(10, 20)],
    #         [x for x in range(20, 30)],
    #         [x for x in range(30, 40)]]
    
    test = [[1]]
    target = 0

    answer = searchMatrix(test, target) # looking for true
    print(answer)
    


def searchMatrix(matrix, target):
    matrix_type = type(matrix)
    if matrix_type == int:
        return target == matrix
    # crops it if its a 2d matrix.
    if matrix_type == list and len(matrix) == 1 :
        matrix = matrix[0]
        return searchMatrix(matrix, target)

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
        return searchMatrix(matrix, target)
    elif number > target:
        matrix = matrix[:pivot]
        return searchMatrix(matrix, target)


    # print(test)
    # print(len(test))
    # test = test[:1]
    # print(test)
    # print(len(test))
    # if len(test) == 1:
    #     test = test[0] 
    # print(test[0])




if __name__ == "__main__":
    main()
