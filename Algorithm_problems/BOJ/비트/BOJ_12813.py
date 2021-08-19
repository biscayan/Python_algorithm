import sys
# return int_num which is inputted as binary form
A = int(sys.stdin.readline().strip(),2)
B = int(sys.stdin.readline().strip(),2)
mask = 2**100000-1
print(bin(A & B)[2:].zfill(100000))
print(bin(A | B)[2:].zfill(100000))
print(bin(A ^ B)[2:].zfill(100000))
print(bin(A ^ mask)[2:].zfill(100000))
print(bin(B ^ mask)[2:].zfill(100000))