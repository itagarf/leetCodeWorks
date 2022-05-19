#Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#Each row must contain the digits 1-9 without repetition.
#Each column must contain the digits 1-9 without repetition.
#Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

#constraints:
#board.length == 9
#board[i].length == 9
#board[i][j] is a digit 1-9 or '.'


from collections import defaultdict

def isValidSudoku(board):
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqre = defaultdict(set)

        bRange = range(0, len(board))

        for r in bRange:
            for c in bRange:                
                bElements = board[r][c]

                if bElements == '.': #the board has empty values represented by a dot, so continue if there's a dot.
                    continue
                #check if there are any duplicates. return false if any is found.
                if bElements in rows[r] or bElements in cols[c] or bElements in sqre[(r // 3, c // 3)]:
                    return False

                rows[r].add(bElements)
                cols[c].add(bElements)
                sqre[(r // 3, c // 3)].add(bElements)

        return True

board1 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


isValidSudoku(board1)


#see https://www.youtube.com/watch?v=TjFXEUCMqI8