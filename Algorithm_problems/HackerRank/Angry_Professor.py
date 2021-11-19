def angryProfessor(k, a):
    cnt = 0
    for num in a:
        if num <= 0:
            cnt += 1
    print("YES" if cnt<a else "NO")
        
if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        a = list(map(int, input().rstrip().split()))
        angryProfessor(k, a)