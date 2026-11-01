class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1st rule

        hash_table = dict()

        for i in range(len(board)):
            temp = set()
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in temp:
                    return False
                temp.add(board[i][j])

                if j in hash_table:
                    if board[i][j] in hash_table[j]:
                        return False
                    else:
                        hash_table[j].add(board[i][j])
                else:
                    hash_table[j] = set()
                    hash_table[j].add(board[i][j])

                l = i // 3
                m = j // 3
                k = str(l) + str(m)

                if k in hash_table:
                    if board[i][j] in hash_table[k]:
                        return False
                    else:
                        hash_table[k].add(board[i][j])
                else:
                    hash_table[k] = set()
                    hash_table[k].add(board[i][j])
        return True
                