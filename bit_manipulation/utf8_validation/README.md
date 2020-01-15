# UTF-8 Validation

[Leetcode 393](https://leetcode.com/problems/utf-8-validation/)

## Problem Statement

A character in UTF8 can be from 1 to 4 bytes long, subjected to the following
rules:

For 1-byte character, the first bit is a 0, followed by its unicode code. For
n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by
n-1 bytes with most significant 2 bits being 10. This is how the UTF-8 encoding
would work:

```text
   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
```

Given an array of integers representing the data, return whether it is a valid utf-8 encoding.

**Note:**

The input is an array of integers. Only the least significant 8 bits of each
integer is used to store the data. This means each integer represents only 1
byte of data.

### Example 1

```text
data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.

Return true.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
```

### Example 2

```text
data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.

Return false.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.
```

## Solution

Bit manipulation at the first byte will determine the encoding. The intuition is
that a bit `AND` a 1 will only produce a 1 if the bit is a 1, otherwise the bit
must have been a 0. Similarly, 0 AND a bit will always "clear" the resulting
bit. For example:

```text
'11' & '00' == '00'
'11' & '01' == '01'
'11' & '10' == '10'
'11' & '11' == '11'

So 1's can be used to "read" bits.
```

Algorithm wise, we read the first byte. From that byte's encoding, determine
whether if it's a 1, 2, 3, or 4 byte character. For the rest of the bytes in
this character, ensure it has the for '10xxxxxx'.

### Time Complexity

`AND` operations are instant. We simpily need to traverse the array of integers.
if `n` is the number of elements in this array, then `O(n)` is our time complexity.

### Space Complexity

There's no extra space used to store anything, so `O(1)`.
