from collections import defaultdict

def longestArithSeqLength(A: List[int]) -> int:
    if len(A) <= 1: return len(A)
    
    # list of dictionary storing {diff -> count}
    count = [defaultdict(int) for _ in range(len(A))]
    max_count = 2   # at least 2

    # initialize first column since the first column have no
    # previous dictionaries to use
    # the first colum represents the 2 itemed sequence at 0 and j
    for j in range(1, len(A)): count[j][A[j] - A[0]] = 2

    # traverse colums
    for i in range(1, len(A)-1):
        # traverse rows
        for j in range(i+1, len(A)):
            diff = A[j] - A[i]
            # since previous sequence ended at index j
            # the current diff from A[j] to A[i] must
            # add on the the sequence that ended at j.
            # if the diff can't be found, start a 2 itemed
            # sequence at j and i
            count[j][diff] = max(2, count[i][diff] + 1)
            # update max_count
            max_count = max(max_count, count[j][diff])
    
    return max_count

