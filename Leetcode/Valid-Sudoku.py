class Solution:
    def isValidSudoku(self, board):
        rows, cols, boxes = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    k = (i // 3) * 3 + (j // 3)
                    if num in rows[i] or num in cols[j] or num in boxes[k]:
                        return False
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[k].add(num)
        return True
