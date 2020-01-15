

# from the first byte encoding, determine the number of additional bytes that
# belong to this UTF8 character.
# valid return values ranges from 0 to 3.
# -1 if the first encoding is invalid.
def bytesCount(num: int) -> int:
    # '0xxxxxxx'
    if 128 & num == 0: return 0
    # '110xxxxx'
    if 224 & num == 192: return 1
    # '1110xxxx'
    if 240 & num == 224: return 2
    # '11110xxx'
    if 248 & num == 240: return 3
    # invalid encoding
    return -1

# return true if num has '10' to start
def hasOneZero(num: int) -> bool:
    # '10xxxxxx'
    return 192 & num == 128

def validUtf8(data: List[int]) -> bool:
    i = 0
    while i < len(data):
        # determine the encoding of this character by reading the first byte
        addBytes = bytesCount(data[i])
        # invalid encoding
        if addBytes == -1: return False
        
        # iterate through the rest of this character's bytes
        for _ in range(addBytes):
            i += 1
            # eliminate index out of bound error
            if i >= len(data): return False
            # check for form '10xxxxxx'
            if not hasOneZero(data[i]): return False
        
        # move on to next character
        i += 1
    
    return True
