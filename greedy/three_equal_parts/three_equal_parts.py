def threeEqualParts(A: List[int]) -> List[int]:
    # invalid input
    if len(A) < 3: return [-1, -1]

    # count the number of 1s
    ones = A.count(1)
    # the list contain only 0s, return any solution
    if ones == 0: return [0, len(A) - 1]
    # the list contains incorrect number of 1s
    # the number of 1s must be divisible by 3
    if ones % 3 != 0: return [-1, -1]

    # assign pointers to the first appearing 1s in each part 
    lp, mp, rp = 0, 0, 0
    # helper counters of 1s
    l0, m0, r0 = ones, ones - (ones//3), ones - 2*(ones//3)
    for i, b in enumerate(A):
        if b == 1:
            # assign pointer locations
            if ones == l0:
                lp = i
            elif ones == m0:
                mp = i
            elif ones == r0:
                rp = i
            ones -= 1

    # ignoring the leading 0s, ensuring significant bits are the same
    # starting for the first appearing 1s in each part
    li, mi, ri = lp, mp, rp
    while ri < len(A):
        if A[li] != A[mi] or A[mi] != A[ri]: return [-1, -1]
        li += 1
        mi += 1
        ri += 1

    return [li-1, mi]

