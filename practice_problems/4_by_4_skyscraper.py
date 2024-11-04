
"""
In a grid of 4 by 4 squares you want to place a skyscraper in each square with only some clues:

The height of the skyscrapers is between 1 and 4
No two skyscrapers in a row or column may have the same number of floors
A clue is the number of skyscrapers that you can see in a row or column from the outside
Higher skyscrapers block the view of lower skyscrapers located behind them

Can you write a program that can solve this puzzle?

Example:

To understand how the puzzle works, this is an example of a row with 2 clues. Seen from the left side there are 4 buildings visible while seen from the right side only 1:

 4	    	    	    	    	 1

There is only one way in which the skyscrapers can be placed. From left-to-right all four buildings must be visible and no building may hide behind another building:

 4	 1	 2	 3	 4	 1


Task:

Finish:
function solvePuzzle(clues)
Pass the clues in an array of 16 items. This array contains the clues around the clock, index:
  	 0	 1	   2	   3	  
 15	  	  	  	  	 4
 14	  	  	  	  	 5
 13	  	  	  	  	 6
 12	  	  	  	  	 7
  	11	10	 9	 8	  
If no clue is available, add value `0`
Each puzzle has only one possible solution
`SolvePuzzle()` returns matrix `int[][]`. The first indexer is for the row, the second indexer for the column. (Python: returns 4-tuple of 4-tuples, Ruby: 4-Array of 4-Arrays)

Problem:
    - To create a function that places skyscrapers on a 4x4 grid 

Rules:
    - input is an array of 16 items with clues
    - the height of the skyscrapers is between 1 and 4
    - no two skyscrapers in a row or column have the same number of floors
    - higher skyscrapers block the view of smaller skyscrapers behind them from left to righ
    - each puzle has only one possible solution
    - clue is the number of skyscrapers seen from outside row

Data:
    Input: array of clues 
    Ouput: 4x4 matrix of ints 

Examples:
    - create 4x4 sollution_matrix with 0s
    - create 4x4 lock_matrix with 0
    - infill locked rows/columns:
        - items with clue of 4
        - items where the sum of clues on both ends = 4
        - items where clues is 1
            - change items to '1' in lock_matrix
            - add items to sollution_matrix
    - while True:
    - cycle through rules for cols checking both ends of the column:
        - if cell is not locked:
            - if clue is not 1 or 4:
                - while true
                    - try combination of number and see if all rule of cells affected are satisfied
                        - check what numbers are available and check agaisnt available numbers below
                            if clue equals 2:
                                - 2,4
                                - 1,4
                                - 3,4
                                - 3,1,4
                                - 3,2,4
                                - 3,2,1,4
                                - 2,1,4
                            if clue equals 3:
                                -2,3,4
                                -1,3,4
                                -1,2,4
                                -2,3,1,4
                                -2,1,3,4
                                -1,3,2,4
                            if solution satisies all conditions of cells then add to solution matrix

        

    - get view (input_list):
        view_count = 1
        for item in input_list:
            if item < next item:
                view_count += 1
        return view_count
        

           1  2
    [ ][ ][4][3]
    [ ][ ][3][4]2
   1[ ][ ][2][ ]
    [ ][ ][1][ ]
           3
"""

class Skyscraper:

    def __init__(self):
        self.grid = [[0,0,0,0] for number in range(0,4)]

    def check_row(self, idx, value_string):

        return all([self.grid[idx][i] == 0 or self.grid[idx][i] == int(number) for i,number in enumerate(value_string)])

    def check_col(self, idx, value_string):

        return all([self.grid[i][idx] == 0 or self.grid[i][idx] == int(number) for i,number in enumerate(value_string)])

    def add_row(self, idx, value_string):

        self.grid[idx] = [int(number) for number in value_string]

    def add_col(self, idx, value_string):

        for i in range(4):
            self.grid[i][idx] = value_string[i]
    
    @staticmethod
    def get_view(string):
        view_count = 1
        for idx,item in enumerate(string):
            if idx < 3 and item < string[idx+1]:
                view_count += 1
        return view_count

"""
- create l
"""

def generate_combinations():

    combo = []

    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                for l in range(1,5):
                    numbers = [i,j,k,l]
                    if len(set(numbers)) == 4:
                        combo.append(''.join([str(number) for number in numbers]))
    
    return {i:combo for i in range(4)}

def get_view(string):
        view_count = 0
        value = 0
        for number in string:
            if int(number) > value:
                view_count += 1
                value = int(number)
        return view_count



def solve_puzzle(clue_list):
    clue_combos = {1: ['4123', '4312', '4231', '4132', '4213','4321'],
                   2: ['2431','2413','1423','1432','3412','3421','3142','3241','3214','2143'],
                   3: ['2341','1342','1243','2314','2134','1324'],
                   4: ['1234']
    }


    row_combos = generate_combinations()
    col_combos = generate_combinations()

    clue_list_col_1 = clue_list[0:4]
    clue_list_col_2 = clue_list[8:12][::-1]

    clue_list_row_1 = clue_list[12::][::-1]
    clue_list_row_2 = clue_list[4:8]

    col_clues = zip(clue_list_col_1,clue_list_col_2)
    row_clues = zip(clue_list_row_1, clue_list_row_2)


    for i,r_clue in enumerate(list(row_clues)):

        if r_clue[0] != 0:

            row_combos[i] = [combo for combo in row_combos[i] if get_view(combo) == r_clue[0]]
        
        if r_clue[1] != 0:

            row_combos[i] = [combo for combo in row_combos[i] if get_view(combo[::-1]) == r_clue[1]]

        for j,c_clue in enumerate(col_clues):

            if c_clue[0] != 0:

                row_combos[i] = [combo for combo in row_combos[i] if (combo[j] in [letter[i] for letter in clue_combos[c_clue[0]]])]
            
            



        


    print(row_combos)


    return None


clues = (
( 2, 2, 1, 3,  
  2, 2, 3, 1,  
  1, 2, 2, 3,  
  3, 2, 1, 3 ),
( 0, 0, 1, 2,   
  0, 2, 0, 0,   
  0, 3, 0, 0, 
  0, 1, 0, 0 )
)

outcomes = (
( ( 1, 3, 4, 2 ),       
  ( 4, 2, 1, 3 ),       
  ( 3, 4, 2, 1 ),
  ( 2, 1, 3, 4 ) ),
( ( 2, 1, 4, 3 ), 
  ( 3, 4, 1, 2 ), 
  ( 4, 2, 3, 1 ), 
  ( 1, 3, 2, 4 ) )
)


print(solve_puzzle (clues[0]) == outcomes[0])
print(solve_puzzle (clues[1]) == outcomes[1])
