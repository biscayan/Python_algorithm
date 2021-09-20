A, B, V = map(int, input().split())
print((V-A)//(A-B)+1) if (V-A) % (A-B) == 0 else print((V-A)//(A-B)+2)