class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                
                box_id = (i // 3, j // 3)
                
                if num in rows[i] or num in cols[j] or num in boxes[box_id]:
                    return False
                
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_id].add(num)
        print(rows)
        return True