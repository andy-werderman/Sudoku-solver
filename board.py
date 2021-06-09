# exec(open("C:/Users/AWerder1/Documents/Sudoku/board.py").read())

class Board:
    '''
    Class for a Sudoku board. The board is a 9x9 grid of cells. Each cell value is either an int between 1 and 9 or a list. An int indicates a set value while a list represents all possible values for the given cell.
    '''
    
    def __init__(self):
        
        # init every cell to have possible values 1..9
        self.grid = [[list(range(1,10)) for i in range(9)] for j in range(9)]

        '''
        1. Take new board instance as input
        2. Read inital cell values from std_in
        3. Set initial board values
        '''

        print("Provide each row of the board below using a single x for an empty cell. Press enter to continue to the next row.")

        # row index
        r = 0

        while (r < 9):
            row = input("Row" + str(r+1) + ": ")

            try: 
                if(len(row) != 9):
                    raise Exception("Input character count not equal to 9.") 

                for c,val in enumerate(row):
                        if val.isnumeric():
                            # string char is forced to be single digit. 
                            # Only numberic invalid char is 0.
                            if (int(val) != 0):
                                self.set_value(r,c,int(val))
                            else:
                                raise Exception("Integer cell value cannot be 0.")

                # increment row index
                r += 1
            except Exception as reason:
                print("ERROR: Bad input. " + str(reason) + " Please try again.")
    # end function

            
    def __str__(self):
        # prints int value for set cells and '*' for non-set cells (lists)
        out = '-'*33 + '\n'
        
        for r,row in enumerate(self.grid):
            for c,val in enumerate(row):
                # use * character to represnt a non-set cell
                if (type(val) == list):
                    val = '*'
                # draw vertical line for square
                if(c%3 == 2):
                    out += str(val) + '  |  '
                else:
                    out += str(val) + '  '
            
            # draw horizontal line for square
            if (r%3 == 2):
                out += '\n' + '-'*33 + '\n'
            else:
                out += '\n'
                
        return out
    # end function
        
        
    def __repr__(self):
        # prints data as is - ie prints both int and list values
        out = '-'*33 + '\n'
        
        for r,row in enumerate(self.grid):
            for c,val in enumerate(row):
                # draw vertical line for square
                if(c%3 == 2):
                    out += str(val) + '  |  '
                else:
                    out += str(val) + '  '
            
            # draw horizontal line for square
            if (r%3 == 2):
                out += '\n' + '-'*33 + '\n'
            else:
                out += '\n'
                
        return out
    # end function
    
    
    def get_row(self,r):
        '''
            input: row index
            output: returns dict containing the cells in the respective row. keys are a tuple of the (row,col) indices in the grid
        '''
        row = dict()
        
        for i in range(9):
            row[(r,i)].append(self.grid[r][i])
        
        return row
    # end function
        
        
    def get_col(self,c):
        '''
            input: col index
            output: returns dict containing the cells in the respective column. keys are a tuple of the (row,col) indices in the grid
        '''
        col = dict()
        
        for i in range(9):
            col[(i,c)].append(self.grid[i][c])
        
        return col
    # end function
    
    
    def get_square(self,r_index,c_index):
        '''
            input: row, col indices
            output: returns dict containing the cells in the respective square. keys are a tuple of the (row,col) indices in the grid
        
            Note: we are numbering each 3x3 square on the soduko board from the top left to bottom right 0-8. 
        '''
        square = dict()
        square_index_mapping = {0:[0,1,2], 1:[0,1,2], 2:[0,1,2], 3:[3,4,5], 4:[3,4,5], 5:[3,4,5], 6:[6,7,8], 7:[6,7,8], 8:[6,7,8]}
        
        # get ranges for square
        rows = square_index_mapping[r_index]
        cols = square_index_mapping[c_index]
        
        # get square values
        for r in rows:
            for c in cols:
                square[(r,c)].append(self.grid[r][c])
        
        return square
    # end function


    def remove_possible_value(self,collection,val):
        # remove value from each possibility list in a given row, col, or square
        for loc in collection:
            if ((type(collection[loc]) == list) and (val in collection[loc])):
                self.grid[loc[0]][loc[1]].remove(val)
    # end function

    
    def set_value(self,r,c,val):
        # set values
        self.grid[r][c] = val
        self.grid[r][c] = val
    
        # remove value as possibility from row col square
        if (type(val) == int):
            row = self.get_row(r)
            col = self.get_col(c)
            square = self.get_square(r,c)

            self.remove_possible_value(row,val)
            self.remove_possible_value(col,val)
            self.remove_possible_value(square,val)
    # end function

        
    def is_complete(self):
        # returns true if for all cells type(cell) == int
        for row in self.grid:
            for cell in row:
                if (type(cell) != int):
                    return False
        return True
    # end function


    def set_obvious_singles(self):
        '''
        find cells whose values is a singleton list. set cell to be that value.
        '''
        done = False
    
        # continue until we cannot replace singleton list with the value anymore
        while(not done):
            done = True

            # iterate through board and replace singleton lists with their value
            for r,row in enumerate(self.grid):
                for c,cell in enumerate(row):
                    if (type(cell) == list) and (len(cell) == 1):
                        # singleton found, call set_value function
                        self.set_value(r,c,cell[0])
                        done = False
    # end function


    def set_obvious_doubles(self):
        return None
    # end function


    def set_obvious_triples(self):
        return None
    # end function