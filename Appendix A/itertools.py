from itertools import permutations # 순열
from itertools import combinations # 조합
from itertools import product # 중복허용 순열
from itertools import combinations_with_replacement # 중복허용 조합

data = ['A', 'B', 'C']

permutation_result = list(permutations(data, 2))
print(permutation_result) # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

combination_result = list(combinations(data, 2))
print(combination_result) # [('A', 'B'), ('A', 'C'), ('B', 'C')]

product_result = list(product(data, repeat=2))
print(product_result) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

combination_repl_result = list(combinations_with_replacement(data, 2))
print(combination_repl_result) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]