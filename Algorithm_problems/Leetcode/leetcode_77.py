from itertools import combinations

def combine(n: int, k: int):
    num_list = [i for i in range(1,n+1)]
    comb_list = list(combinations(num_list,k))
    return comb_list