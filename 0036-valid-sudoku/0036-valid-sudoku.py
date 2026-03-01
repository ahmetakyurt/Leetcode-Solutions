class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for n in range(9)]
        columns = [set() for n in range(9)]
        blocks = [[set() for _ in range(3)] for i in range(3)]
        for row in board:
            print(row)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if board[i][j] in rows[i]:
                    return False
                else:
                    rows[i].add(board[i][j])      
                
                if board[i][j] in columns[j]:
                    return False
                else:
                    columns[j].add(board[i][j])

                blockRow = i // 3
                blockColumn = j // 3

                if board[i][j] in blocks[blockRow][blockColumn]:
                    return False
                else:
                    blocks[blockRow][blockColumn].add(board[i][j])
        return True

            
                        
            