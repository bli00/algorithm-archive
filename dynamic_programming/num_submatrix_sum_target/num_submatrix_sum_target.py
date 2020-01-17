from typing import List

def numSubmatrixSumTarget(matrix: List[List[int]], target: int) -> int:
    width, height = len(matrix[0]), len(matrix)
    for i in range(height):
        for j in range(1,width):
            matrix[i][j] += matrix[i][j-1]

    res = 0
    for l in range(width):
        for r in range(l,width):
            occurences = {0:1}
            sums = 0
            for i in range(height):
                sums += matrix[i][r] - (matrix[i][l-1] if l > 0 else 0)
                res += occurences.get(sums-target, 0)
                occurences[sums] = occurences.get(sums, 0) + 1

    return res

