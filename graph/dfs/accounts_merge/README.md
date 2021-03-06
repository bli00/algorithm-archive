# Accounts Merge

[LeetCode Problem 721](https://leetcode.com/problems/accounts-merge/)

## Problem Statement

Given a list accounts, each element `accounts[i]` is a list of strings, where the first element `accounts[i][0]` is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the
first element of each account is the name, and the rest of the elements are
emails in sorted order. The accounts themselves can be returned in any order.

### Example 1

```text
Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]

Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]

Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
```

### Note

* The length of accounts will be in the range `[1, 1000]`.
* The length of `accounts[i]` will be in the range `[1, 10]`.
* The length of `accounts[i][j]` will be in the range `[1, 30]`.

## Solution

My first instinct was to simply traverse the lists while marking each email with
a pointer to the corresponding person it represents. When visiting an email that
has been seen, update both pointers to point to the same person. But this
approach won't work since the accounts entries are basically bi-directional
graphs and traversing the emails in this manner limits acount merges into an
"uni-directional" merge. So we must consider this problem as a graph traversal
problem, where each entry in the list of accounts is a node, and two accounts
are "merged" when they belong to the same component.

The idea is to first construct a bi-directional adjacency matrix. From this
matrix, find all of the strongly connected components by DFS (BFS would also
work) and merge all the accounts that belong to the same component.

Algorithm wise, we use the index of the account in the `accounts` list as
representation of their nodes indices. We use a dictionary named `emails`,
consisting of `email -> node index` mapping to keep track of the edges. Adding
emails to `emails` as we traverse the emails in `accounts`. When we encounter an
email that exists in the dictionary, it means that the current node has an edge
to the existing email's node, so we add this edge to the adjacency matrix.

Traversing the graph with DFS requires a for-loop for every node index in the
graph. We start a DFS search with every unvisited node. Every node traversed by
this DFS are in the same component, so they must be the same account. We merge
the emails under this node into a list using an inordered insertion. Once the
DFS terminates, prepend the account holder's name to this list and move on to
the next unvisited node.

### Time complexity

TODO

### Space complexity

The adjacency matrix should be trivial assuming there's more emails under an
`accounts` entry than the total number of entries. In which case the `emails`
dictionary supresses `adj` as the primary space bottleneck. Disregarding `res`,
the space complexity comes out to be `O(n)` with `n` being the total number of
emails in `accounts`.
