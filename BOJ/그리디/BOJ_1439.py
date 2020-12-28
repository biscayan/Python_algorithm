import sys

sys.stdin = open("input.txt","r")

def Reverse(num_seq):
    
    count_zero = 0
    count_one = 0

    for i in range(1,len(num_seq)):

        ### 10이 등장하면 1sequence 뒤집기
        if num_seq[i-1] == "1" and num_seq[i] == "0":
            count_one += 1

        ### 01이 등장하면 0sequence 뒤집기
        elif num_seq[i-1] == "0" and num_seq[i] == "1":
            count_zero += 1

    ### 마지막에 남은 숫자에 따라서 그 sequence를 뒤집기
    if num_seq[-1] == "0":
        count_zero += 1
    else:
        count_one += 1

    return min(count_zero, count_one)


if __name__ == '__main__':

    ###sys.stdin.readline()으로 데이터를 입력받으면 틓림
    sequence = sys.stdin.readline().strip()
    #sequence = input()
    
    print(Reverse(sequence))