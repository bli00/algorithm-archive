# Number of Submatrices That Sum to Target

[Leetcode Problem 1074](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/)

## Problem Statement

Given a `matrix`, and a `target`, return the number of non-empty submatrices that sum to target.

A submatrix `x1, y1, x2, y2` is the set of all cells `matrix[x][y]` with `x1 <= x <= x2` and `y1 <= y <= y2`.

Two submatrices `(x1, y1, x2, y2)` and `(x1', y1', x2', y2')` are different if they have some coordinate that is different: for example, if `x1 != x1'`.

### Example 1

```text
Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.
```

### Example 2

```text
Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
```

### Note

1. `1 <= matrix.length <= 300`
2. `1 <= matrix[0].length <= 300`
3. `-1000 <= matrix[i] <= 1000`
4. `-10^8 <= target <= 10^8`

## Solution

It's better to illustrate the solution with an example. Consider
[Example 1](#example-1):

First calculate the prexfixed sums of each row. A prefixed sum is a list of
running sums for every element of the list. `prefix[i][r]` is equivalent to
`sum(matrix[i][0],...,matrix[i][r])`.

```text
Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0

output: prefix = [[0,1,1],[1,2,3],[0,1,1]]
```

Observe that `prefix[i][l] - prefix[i][r] = sum(matrix[i][l+1],...,matrix[i][r])` and `prefix[i][l] - prefix[i][l-1] = matrix[i][l]`.

Now consider the prefixes in rows. That is, start changing `i`. We observe that `prefix[0][1] + prefix[1][1]` is the sum of the `2x2` submatrix
on the top left. Similarly `prefix[0][1] + prefix[1][1] + prefix[2][1]` is the
sum of the `3x2` submatrix on the left.

Since `prefix[i][l] - prefix[i][r] = sum(matrix[i][l+1],...,matrix[i][r])`. We
can vary `l` and `r` to sum any submatrices.

For the final trick, when vertically summing up prefixes. That is, looping
through `i`. We keep a dictionary named `occurences` that stores the vertical
running sum and the number of times it's been encounter. At some row index `i`,
we can deduce that is there is submatrix that sums up to `target` by checking the
value of `sum - target` in the `occurences` dictionary. If there is a submatrix
from row `j` to `i` that sums up to target, then the running sum at index `j`
must have been recorded in `occurences` previously.

### Time Complexity

The prefix calculation takes `O(m*n)` time. The triple for-loop takes O(m*n^2)
time.

### Space Complexity

`occurences` is a dictionary that's used to keep track of previous running sums.
This can grow up to `m` where `m` is the height of the matrix.

The prefixes are stored in place by changing `matrix`. If we're not allow to
modify `matrix`, then an extra `O(m*n)` space is needed.
