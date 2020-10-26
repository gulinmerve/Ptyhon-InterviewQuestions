def f_word(board, word):
    def check_adj(r,c,pos,visited):
        if not (r>=0 and r < len(board) and c >= 0 and c < len(board[0]) and pos < len(word)): return False
        if (r,c) in visited: return False
        if board[r][c] != word[pos]: return False
        if pos == len(word) - 1: return True
        visited.add((r,c))
        for i in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            if check_adj(r+i[0],c+i[1],pos+1,visited):
                return True
        visited.remove((r,c))
        return False
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == word[0]:
                if check_adj(r,c,0,set()):
                    return True
    return False