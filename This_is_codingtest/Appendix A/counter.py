from collections import Counter

array = ['Red','Blue','Green','Blue','Blue','Green','Red','Red','Blue']
counter = Counter(array)

print(counter['Red']) # 3
print(counter['Blue']) # 4
print(counter['Green']) # 2
print(dict(counter)) # {'Red': 3, 'Blue': 4, 'Green': 2}