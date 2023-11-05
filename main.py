import math

def coin_change(den :list[int], tgt: int):
    mem : dict[tuple[int, int], float] = {}
    def dp(i :int, tgt : int) -> float:
        if (i, tgt) in mem:
            return mem[(i,tgt)]
        if i < 0:
            return math.inf
        rmnd = tgt - den[i]
        if rmnd == 0:
            return 1
        elif rmnd < 0:
            return dp(i-1, tgt)
        mem[(i,tgt)] =  min(
            1 + dp(i, rmnd),
            dp(i-1, tgt),
        )
        return mem[(i,tgt)]
    return dp(len(den)-1, tgt)

if __name__ == '__main__':
    print(coin_change([1,5,12,19], 77))