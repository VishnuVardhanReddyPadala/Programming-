class Solution:
    def solve(self, board):
        if not board:
            return

        def dfs(i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != 'O':
                return
            board[i][j] = 'S'
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                dfs(x, y)

        for i in range(len(board)):
            for j in [0, len(board[0])-1]:
                if board[i][j] == 'O':
                    dfs(i, j)
        for j in range(len(board[0])):
            for i in [0, len(board)-1]:
                if board[i][j] == 'O':
                    dfs(i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'
