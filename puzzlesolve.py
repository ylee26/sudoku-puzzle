def check_zero(puzzle):
    """
    Helper that creates a 1D version of the nested 2D lists. This allows the 
    detection of 0's easier. Returns a boolean indicating whether or not 0 is in
    the Sudoku puzzle.  
    """
    spread_list = []
    for x in range(9):
        for y in range(9):
            spread_list.append(puzzle[x][y])
    return 0 in spread_list

def loop_hori(linear_list,num_to_check):
    """
    Loops through a one-dimensional list to see if there are any overlaps 
    between certain numbers. Returns a boolean. If num_to_check is in 
    linear_list, then this function returns False. 

    Parameter linear_list: linear_list is a list that contains the numbers
    ranging through 0~9
    Precondition: linear_list is a list that contains numbers 0~9
    """
    return not num_to_check in linear_list

def loop_vert(puzzle,num_to_check,col_to_loop):
    """
    Loops through one column of a nested loop to see if there are any 
    overlaps between certain numbers. Returns a boolean. If num_to_check
    is in the column that this function is checking, this function returns 
    False.
    """
    temp_list = [] 
    for x in range(9):
        temp_list.append(puzzle[x][col_to_loop])
        
    if num_to_check in temp_list:
        return False
    return True

def loop_box(puzzle,num_to_check,x_position,y_position):
    """
    Loops through the 3X3 box that the number being loops is confined in
    to check if there are any overlaps. Returns True if there are none. 

    Parameter
    Precondition
    """
    temp_list = []
    # First column of 3X3
    if x_position<3 and y_position<3:
        for i in range(3):
            for j in range(3):
                temp_list.append(puzzle[i][j])
        
    elif x_position>=3 and x_position<6 and y_position<3:
        for i in range(3,6):
            for j in range(3):
                temp_list.append(puzzle[i][j])
        
    elif x_position>=6 and y_position<3:
        for i in range(6,9):
            for j in range(3):
                temp_list.append(puzzle[i][j])
        
    # Second column of 3X3
    elif x_position<3 and y_position>=3 and y_position<6:
        for i in range(3):
            for j in range(3,6):
                temp_list.append(puzzle[i][j])
        
    elif x_position>=3 and x_position<6 and y_position>=3 and y_position<6:
        for i in range(3,6):
            for j in range(3,6):
                temp_list.append(puzzle[i][j])

    elif x_position>=6 and y_position>=3 and y_position<6:
        for i in range(6,9):
            for j in range(3,6):
                temp_list.append(puzzle[i][j])
        
    # Third column of 3X3
    elif x_position<3 and y_position>=6:
        for i in range(3):
            for j in range(6,9):
                temp_list.append(puzzle[i][j])
        
    elif x_position>=3 and x_position<6 and y_position>=6:
        for i in range(3,6):
            for j in range(6,9):
                temp_list.append(puzzle[i][j])

    elif x_position>=6 and y_position>=6:
        for i in range(6,9):
            for j in range(6,9):
                temp_list.append(puzzle[i][j])
    
    return not num_to_check in temp_list

def help_correct(puzzle,row,col,num):
    """
    Checks for Sudoku puzzle slots with a single choice left. 
    """
    if loop_hori(puzzle[row],num) and loop_vert(puzzle,num,col) and \
        loop_box(puzzle,num,row,col):
        return True
    return False

def find_empty(puzzle):
    """
    Finds a cell that is empty in the Sudoku puzzle and returns a tuple with 
    that row and column. Returns None otherwise. 
    """
    for row in range(9):
        for col in range(9):
            if puzzle[row][col]==0:
                return row, col
    
    return -1,-1

def backtrack(puzzle):
    """
    Recursive function that backtracks the Sudoku puzzle through a trial and 
    error process to solve the Sudoku.
    """
    row,col = find_empty(puzzle)

    if row == -1:
        return True

    for num_to_check in range(1,10):
        if help_correct(puzzle,row,col,num_to_check):
            puzzle[row][col]=num_to_check
            if backtrack(puzzle):
                return True

        puzzle[row][col]=0

    return False
    
    

if __name__=='__main__':
    puzzle = [
        [8, 0, 0, 0, 2, 0, 0, 0, 0], 
        [3, 4, 0, 0, 0, 1, 0, 0, 0], 
        [0, 0, 6, 0, 0, 3, 0, 9, 0], 
        [0, 0, 2, 6, 8, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 9, 0, 0, 0], 
        [5, 0, 0, 0, 0, 4, 1, 6, 0], 
        [0, 0, 5, 0, 4, 2, 0, 8, 7], 
        [4, 2, 0, 0, 0, 8, 0, 0, 0], 
        [6, 0, 0, 1, 0, 0, 2, 0, 4]
        ]

    backtrack(puzzle)
    print("Here is the puzzle")
    print(puzzle)
    