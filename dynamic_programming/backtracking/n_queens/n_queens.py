from typing import List

def solveNQueens(n: int) -> List[List[str]]:
    # legal placements to be converted
    placements = []

    # iterate through each row and find viable placements
    # the current row can be inferred from 'queens'
    # queens[i] -> j: index is the row, element is the column
    # sums contains i + j values
    # difs contains i - j values
    def queenSolver(queens: List[int], sums: List[int], difs: List[int]):
        i = len(col) # infer current row
        if i == n:
            # base case
            placements.append(queens.copy())
            return
        
        for j in range(n):
            # find all viable columns for placements
            if j not in queens and i+j not in sums and i-j not in difs:
                # backtracking method to save space
                queens.append(j)
                sums.append(i+j)
                difs.append(i-j)

                # recurse on possible values
                queenSolver(queens, sums, difs)

                # backtrack to prepare for next iteration
                queens.pop()
                sums.pop()
                difs.pop()

    dfs([],[],[])

    # construct result
    return [[('.'*j + 'Q' + '.'*(n-j-1)) for j in p] for p in placements]