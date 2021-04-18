import sys

sys.stdin = open("input.txt","r")

alphabet_seq1 = input()
alphabet_seq2 = input()

alphabet_dict1 = {}
alphabet_dict2 = {}

###dictionary에 value추가 방법1(강의의 방식)
for alphabet in alphabet_seq1:
    alphabet_dict1[alphabet] = alphabet_dict1.get(alphabet,0) + 1

###dictionary에 value추가 방법2(나의 방식)
for alphabet in alphabet_seq2:
    if alphabet in alphabet_dict2:
        alphabet_dict2[alphabet] += 1
    else:
        alphabet_dict2[alphabet] = 1

###강의의 방식
for i in alphabet_dict1.keys():
    if i in alphabet_dict2.keys():
        ###value값이 다를 때
        if alphabet_dict1[i] != alphabet_dict2[i]:
            print("NO")
            break
    ###key가 없을 때
    else:
        print("NO")
        break
else:
    print("YES")

###나의 방식1
alphabet_list1 = sorted(alphabet_dict1.items())
alphabet_list2 = sorted(alphabet_dict2.items())

if alphabet_list1 == alphabet_list2:
    print("YES")
else:
    print("NO")

###나의 방식2
for i in range(len(alphabet_list1)):
    if alphabet_list1[i][1] != alphabet_list2[i][1]:
        print("NO")
        break
else:
    print("YES")