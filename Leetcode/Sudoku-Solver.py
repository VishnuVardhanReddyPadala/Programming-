class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + (c // 3)].add(num)

        def is_valid(r, c, num):
            return num not in rows[r] and num not in cols[c] and num not in boxes[(r // 3) * 3 + (c // 3)]

        def solve():
            min_choices = float('inf')
            min_pos = None

            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        choices = 0
                        for num in '123456789':
                            if is_valid(r, c, num):
                                choices += 1
                        if choices < min_choices:
                            min_choices = choices
                            min_pos = (r, c)

            if min_pos is None:
                return True

            r, c = min_pos
            for num in '123456789':
                if is_valid(r, c, num):
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + (c // 3)].add(num)
                    if solve():
                        return True
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[(r // 3) * 3 + (c // 3)].remove(num)

            return False

        solve()
