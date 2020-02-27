def alphabetBoardPath(target: str) -> str:
    board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
    coordinates = {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            coordinates[board[i][j]] = (i,j)
    
    cur = (0,0)
    res = ''
        
    for c in target:
        x, y = cur
        m, n = coordinates[c]
        
        if c == 'z':
            res += abs(n-y) * ('R' if n-y > 0 else 'L')
            res += abs(m-x) * ('D' if m-x > 0 else 'U')
        else:
            res += abs(m-x) * ('D' if m-x > 0 else 'U')
            res += abs(n-y) * ('R' if n-y > 0 else 'L')
        res += '!'
        
        cur = (m,n)
    
    return res

