from typing import List

def numSubmatrixSumTarget(matrix: List[List[int]], target: int) -> int:
    width, height = len(matrix[0]), len(matrix)

    # calculate prefix sums
    # a prefix[i] is the total sum of the row from 0 to i
    # prefix[i] - prefix[j] with i > j is the sum of the row from j+1 to i
    for i in range(height):
        for j in range(1,width):
            matrix[i][j] += matrix[i][j-1]

    res = 0
    
    # iterate through possible left and right indices
    # [l=left, r=right]
    for l in range(width):
        for r in range(l,width):
            # keep a dictionary of running sums. If there exist a
            # submatrix that sums to the target. Then the current 
            # running sum minus the target must be a previous running sum
            # `occurences` keeps track of the previous running sums and 
            # the number of times it's occured.
            occurences = {0:1}
            sums = 0

            for i in range(height):
                sums += matrix[i][r] - (matrix[i][l-1] if l > 0 else 0)
                
                # check previous running sums for target submatrices
                res += occurences.get(sums-target, 0)

                # record current running sum
                occurences[sums] = occurences.get(sums, 0) + 1

    return res

