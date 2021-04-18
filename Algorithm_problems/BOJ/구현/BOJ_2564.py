import sys

sys.stdin = open("input.txt", "r")

### 위치를 좌표개념으로 바꿈
def convert_location(location):

    direction = location[0]
    distance = location[1]

    ### 1->북 / 2->남 / 3->서 / 4->동
    if direction == 1:
        location = [0,distance]
    elif direction == 2:
        location = [height, distance]
    elif direction == 3:
        location = [distance,0]
    elif direction == 4:
        location = [distance,width]

    return location


def guard(store_list, person):

    converted_person = convert_location(person)

    ### 둘레
    total = 2 * (width + height)
    
    answer = 0

    for store in store_list:

        converted_store = convert_location(store)
        count = 0

        ### 경비원을 만날때까지 시계방향으로 이동
        while converted_store != converted_person:
            ### (0,y) 북
            if converted_store[0] == 0 and converted_store[1] < width:
                converted_store[1] += 1
                count += 1
            ### (x,width) 동
            if converted_store[0] < height and converted_store[1] == width:
                converted_store[0] += 1
                count += 1
            ### (height, y) 남
            if converted_store[0] == height and converted_store[1] > 0:
                converted_store[1] -= 1
                count += 1
            ### (x,0) 서
            if converted_store[0] > 0 and converted_store[1] == 0:
                converted_store[0] -= 1
                count += 1

        ### 시계방향과 반시계방향 중에서 최소값을 가져옴
        min_dist = min(total-count, count)

        answer += min_dist
    
    return answer


if __name__ == '__main__':

    width, height = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())

    store_list = []

    for _ in range(n):
        store = tuple(map(int, sys.stdin.readline().split()))
        store_list.append(store)

    person = tuple(map(int, sys.stdin.readline().split()))

    print(guard(store_list, person))