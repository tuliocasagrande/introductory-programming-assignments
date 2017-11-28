class GravityPuzzleEasy:
    def solve(self, board):
        new_board = [list(row) for row in board]

        for i in range(len(board)-1, 0, -1):
            for j in range(len(board[i])):
                if new_board[i][j] == '.' and new_board[i - 1][j] == '#':
                    k = i
                    while k < len(board) and new_board[k][j] == '.':
                        new_board[k][j] = '#'
                        new_board[k - 1][j] = '.'
                        k += 1

        return [''.join(row) for row in new_board]
