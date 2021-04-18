import sys

sys.stdin=open("input.txt","r")

def extract_num(seq):
    num_list=[]
    num=0
    div_count=0

    #extract numbers
    for s in seq:
        if s.isdigit()==True:
            num=num*10+int(s)
            #num_list.append(s) 

    #num리스트를 만들어서 진행하는 것도 가능
    '''
    #make a number
    for i in range(len(num_list)):
        num+=int(num_list[i])*(10**(len(num_list)-1-i))
    '''

    #extract aliquot
    for div in range(1,num+1):
        if num%div==0:
            div_count+=1
    
    print(num)
    print(div_count)
    
sequence=input()
extract_num(sequence)