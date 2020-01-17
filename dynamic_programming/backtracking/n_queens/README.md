# N-Queens

[Leetcode Problem 51](https://leetcode.com/problems/n-queens/)

## Problem Statement

The n-queens puzzle is the problem of placing n queens on an `n×n` chessboard such that no two queens attack each other.

Given an integer `n`, return **all** distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens'
placement, where 'Q' and '.' both indicate a queen and an empty space
respectively.

### Example

```text
Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens
```

## Solution

First, observe that each row must have exactly one queen. Similarly, each column
must have exactly one queen.

We can regard every diagonal as a function of `y = mx + b`, where `m` is the
slope and `b` is the y-intercept. Since the diagonals will only have a slope of
either `1` or `-1`. we have the functions `y = x + b` and `y = -x + b`, which
implies `y + x = b` and `y - x = b`. A coordinate `(x',y')` on the same diagonal
will have the same y-intercept as `(x,y)`. Solving for `b` gives us `x + y = x' + y'` and `y - x = y' - x'`. This is critial information that will be used to
infer legal queen placements.

Algorithm wise, since every row has to have exactly one queen. We iterate
through the rows to find a column that's not under attack. Attempt to place a
queen on this (row, column) combination, and let the recursion take care of
itself. We can do this using the information described in the previous
paragraphs.

More specifically, we keep a list `queens` of column numbers. The indices of
`queens` will correspond to the row of that placement whereas the element will
correspond to the column. We also keep a list of `x + y` and `x - y` values to
indicate the squares that are under attack, call these `sums` and `difs`. When
there is a coordinate `(x', y')` we'd like to place a queen on, we check that
`x'` is not in `queens`, `x' + y'` is not in `sums`, and `x' - y'` is not in
`difs`.

We use a backtracking method to save space. That is, we first prepare for the
next recursion by updating `queens`, `sums`, and `difs`. After the current queen
placement, we backtrack and remove the updates to `queens`, `sums`, and `difs`.
Since the updates were inorder, the lists can be treated as a stack.

Finally, the base case is when we have finished traversing all `n` rows. This
can be inferred from the size of `queens`.

### Time Complexity

TODO

### Space Complexity

TODO
