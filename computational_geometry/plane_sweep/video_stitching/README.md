# Video Stitching

[Leetcode problem 1024](https://leetcode.com/problems/video-stitching/)

## Problem Statement

You are given a series of video clips from a sporting event that lasted T
seconds.  These video clips can be overlapping with each other and have varied
lengths.

Each video clip `clips[i]` is an interval: it starts at time `clips[i][0]` and
ends at time `clips[i][1]`.  We can cut these clips into segments freely: for
example, a clip `[0, 7]` can be cut into segments `[0, 1] + [1, 3] + [3, 7]`.

Return the minimum number of clips needed so that we can cut the clips into
segments that cover the entire sporting event `([0, T])`.  If the task is
impossible, return `-1`.

### Example 1

**Input**: `clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10`

**Output**: `3`

**Explanation**: We take the clips `[0,2], [8,10], [1,9]`; a total of `3` clips.
Then, we can reconstruct the sporting event as follows: We cut `[1,9]` into
segments `[1,2] + [2,8] + [8,9]`. Now we have segments `[0,2] + [2,8] + [8,10]`
which cover the sporting event `[0, 10]`.

### Example 2

**Input**: `clips = [[0,1],[1,2]], T = 5`

**Output**: `-1`

**Explanation**: We can't cover `[0,5]` with only `[0,1]` and `[0,2]`.

### Example 3

**Input**: `clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T = 9`

**Output**: `3`

**Explanation**: We can take clips `[0,4]`, `[4,7]`, and `[6,9]`.

### Example 4

**Input**: `clips = [[0,4],[2,8]], T = 5`

**Output**: `2`

**Explanation**: Notice you can have extra video after the event ends.

## Solution

First sort the clips according the starting point. Then we can perform a plane sweep across the intervals. Intuition for this maneuver is that as the plane sweeps across, the intervals intersecting with the plane are clip contents that are in sync. Example 1 can be visualized as the following:

```text
input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10

after scorting:
0  1  2  3  4  5  6  7  8  9  10
[-----]
   [-----------------------]
   [-----------]
            [-----]
               [-----------]
                        [-----]
```

As the plane sweeps from left to right, we greedily select the next interval that has the farthest ending point. The intuition for this is that if the next interval can't cover some gap, then a smaller interval certainly can't neither.

In the above example, the second interval we select should be the interval `[1,9]`, if the ending point `9` lands on some point `t` that can't be covered by an interval, selecting smaller intervals to cover for the distance between `[0,9]` can't be of help.

Algorithm wise, for the current interval we have selected, find all intervals that have a starting point that lands within the current interval. Amongst these select one with the farthest ending point for the next interval we select. By the end we return a count of the intervals we've selected.

### Time Complexity

The biggest bottleneck is the sorting since the plane sweep only takes linear time. So `O(n*log(n))` is the time complexity.

### Space Complexity

Sorting happens in place so the space complexity is constant. `O(1)`.

