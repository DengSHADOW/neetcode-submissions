from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols, rows, squares = defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                
                skey = (r//3, c//3)

                # check existence
                if (num in rows[r] or
                    num in cols[c] or
                    num in squares[skey]):
                    return False

                rows[r].add(num)
                cols[c].add(num)
                squares[skey].add(num)
        return True