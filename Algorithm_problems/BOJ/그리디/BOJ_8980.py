import sys

sys.stdin = open("input.txt", "r")

def delivery(deliver_list):

    answer = 0

    for i in range(M):

        start, destination, boxes = deliver_list[i][0], deliver_list[i][1], deliver_list[i][2]
        cur_boxes = C

        for j in range(start, destination):
            cur_boxes = min(village_list[j], cur_boxes)

        cur_boxes = min(boxes, cur_boxes)

        for j in range(start, destination):
            village_list[j] -= cur_boxes
        
        answer += cur_boxes

    return answer


if __name__ == '__main__':

    N, C = map(int, sys.stdin.readline().split())
    M = int(sys.stdin.readline())

    deliver_list = []
    village_list = [C for _ in range(N+1)] 

    for _ in range(M):
        start, end, box = map(int, sys.stdin.readline().split())
        deliver_list.append((start, end, box))

    ### 빨리 도착하는 마을 순서로 정렬
    deliver_list.sort(key=lambda x:x[1])

    print(delivery(deliver_list))