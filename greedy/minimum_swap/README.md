# Minimum Swaps to Make Strings Equal

[Leetcode problem 1247](https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/)

## Problem Statement

You are given two strings `s1` and `s2` of equal length consisting of letters "x" and "y" only. Your task is to make these two strings equal to each other. You can swap any two characters that belong to different strings, which means: swap `s1[i]` and `s2[j]`.

Return the minimum number of swaps required to make `s1` and `s2` equal, or return `-1` if it is impossible to do so.

### Example 1

```text
Input: s1 = "xx", s2 = "yy"
Output: 1
Explanation: 
Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".
```

### Example 2

```text
Input: s1 = "xy", s2 = "yx"
Output: 2
Explanation: 
Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
Note that you can't swap s1[0] and s1[1] to make s1 equal to "yx", cause we can only swap chars in different strings.
```

### Example 3

```text
Input: s1 = "xx", s2 = "xy"
Output: -1
```

### Example 4

```text
Input: s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
Output: 4
```

## Solution

The characters in this problem are binary. Therefore, a mismatch cannot be fixed unless there's another mismatch to pair. And only exactly one other mismatch is needed. Our solution will attempt to find mismatches by pairs in a greedy manner.

There are two types of mismatched pairs. Highlighted by example 1 and 2.

```text

Type 1: 
'xx' and 'yy' requires exactly 1 swap to fix.

Type 2:
'xy' and 'yx' requires exactly 2 swaps to fix.
```

Our algorithm will attempt to find as many type 1 mismatches pairs as possible. That is, when there is a mismatch, our algorithm will attempt to find another that is mismatched in the same way.

Since the characters are binary, we only need to store one character from one of the strings. That is, we only need to count the mismatched 'x' and 'y' in `s1`. Then we can determine the number of swaps by the parity of both counts. Call these counts `xs` and `ys`.

Since the mismatches need to come in pairs, a odd total count of mismatches indicates that the strings cannot be repaired. So our 'x' and 'y' mismatch counts need to be either both odd or both even.

When both counts are even, we know that we can greedily pair all of them into type 1 mismatches. So we will need `(xs + ys) / 2` swaps. When both counts are odd, we can pair `(xs - 1) + (ys - 1)` of them into type 1 mismatches, so that's `((xs - 1) / 2) + ((ys - 1) / 2)` swaps. The two mismatch left over will need `2` additional swaps to complete.

### Time Complexity

Very obvious that this is a linear time algorithm.

### Space Complexity

No extra space is needed so this is a constant space complexity.

