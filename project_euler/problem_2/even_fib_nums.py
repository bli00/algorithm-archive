def even_fib_num(n: int) -> int:
    a, b = 1, 2
    s = 0
    while b <= n:
        if b % 2 == 0: s += b
        a, b = b, a+b
    
    return s

