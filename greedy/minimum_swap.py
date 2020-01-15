def minimumSwap(self, s1: str, s2: str) -> int:
    if len(s1) != len(s2): return -1
    
    xs, ys = 0, 0 # 'x' mismatch count, 'y' mismatch count
    for i in range(len(s1)):
        # record mismatched 'x' and 'y'
        if s1[i] != s2[i]:
            if s1[i] == 'x':
                xs += 1
            else:
                ys += 1
    
    # the two strings are only matchable if there is an even number of
    # total mismatches.
    # an odd number means there is a mismatch that can't find a replacement
    if (xs + ys) % 2 != 0: return -1

    # mismatched 'x' and 'y' both have an even count
    if xs % 2 == 0: return (xs + ys) // 2

    # mismatched 'x' and 'y' both have an odd count
    return ((xs + ys) // 2) + 1 

