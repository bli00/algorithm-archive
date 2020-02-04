def multiples_of_3_and_5(n: int) -> int:
    if n < 0: return -1
    def arith_series(k: int) -> int:
        return (k*(k+1))//2

    return 3*arith_series((n-1)//3) + 5*arith_series((n-1)//5) - 15*arith_series((n-1)//15)

