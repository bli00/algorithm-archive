from typing import List
import bisect
import collections

def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    adj = [set() for _ in accounts]
    emails = {} # email -> index
    for i, account in enumerate(accounts):
        for e in account[1:]:
            if e in emails: 
                adj[i].add(emails[e])
                adj[emails[e]].add(i) # bi-directional
            emails[e] = i

    s, res = [], []
    for i in reversed(range(len(adj))):
        if adj[i] is not None:
            res.append([])
            s.append(i)
            while s:
                cur = s.pop()
                if adj[cur] is not None:
                    for e in accounts[cur][1:]:
                        if emails[e] != -1:
                            bisect.insort_left(res[-1], e)
                            emails[e] = -1
                    for n in adj[cur]: s.append(n)
                    adj[cur] = None
            res[-1][0:0] = [accounts[i][0]]

    return res
