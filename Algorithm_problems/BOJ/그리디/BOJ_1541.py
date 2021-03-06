import sys

sys.stdin = open("input.txt","r")

# 숫자들을 +한 다음 -를 해줘야 가장 작은 값이 만들어짐
def Calculation(calc_list):

    num_list = []

    for calc in calc_list:
        if "+" in calc:
            init_num = 0
            split_by_plus = calc.split("+")
            for num in split_by_plus:
                init_num += int(num)
            num_list.append(init_num)
        else:
            num_list.append(int(calc))

    result = num_list[0]

    for i in range(1,len(num_list)):
        result -= num_list[i]
        
    print(result)

if __name__ =='__main__':
    calculation = sys.stdin.readline()
    split_by_minus = calculation.split("-")
    Calculation(split_by_minus)