# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
#
# Example:
#
# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above.

from typing import List

res = []
curr = [] # location of queens
occupied = {} # squares that's illegal
traversed = set()
N = 0

# adds a solution on res
def addToAnswer():
    ans = [None] * N

    for q in curr:
        (i, j) = q
        row = ['Q' if k == j else '.' for k in range(N)]
        ans[i] = ''.join(row)

    res.append(ans)

def solveNQueensHelp(n: int):
    # print(res, curr, occupied, N)
    global curr, occupied
    if n == 0:
        addToAnswer()
        return

    directions = {(1,0), (-1,0), (0,-1), (0,1), (-1,-1), (1,1), (-1,1), (1,-1)}
    for i in range(N):
        for j in range(N):
            cell = (i,j)
            if occupied[cell] == 0:
                # try to place a queen here
                if frozenset(curr + [cell]) not in traversed:
                    curr.append(cell)
                    backtracker = []

                    # mark illegal locations
                    for (a,b) in directions:
                        currCell = cell
                        while currCell[0] >= 0 and currCell[0] < N and currCell[1] >= 0 and currCell[1] < N:
                            # print(occupied)
                            occupied[currCell] += 1
                            backtracker.append(currCell)
                            currCell = (currCell[0]+a,currCell[1]+b)

                    solveNQueensHelp(n-1)

                    # backtrack
                    traversed.add(frozenset(curr))
                    curr.pop()
                    for currCell in backtracker:
                        occupied[currCell] -= 1
                
def solveNQueens(n: int) -> List[List[str]]:
    if n < 1:
        return []
    global N
    N = n
    for i in range(N):
        for j in range(N):
            occupied[(i,j)] = 0

    solveNQueensHelp(n)
    return res

res = []
curr = [] # location of queens
occupied = {} # squares that's illegal
traversed = set()
N = 0
print(solveNQueens(2))
res = []
curr = [] # location of queens
occupied = {} # squares that's illegal
traversed = set()
N = 0
print(solveNQueens(3))
res = []
curr = [] # location of queens
occupied = {} # squares that's illegal
traversed = set()
N = 0
print(solveNQueens(4))
res = []
curr = [] # location of queens
occupied = {} # squares that's illegal
traversed = set()
N = 0
print(solveNQueens(5))
