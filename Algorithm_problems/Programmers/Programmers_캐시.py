from collections import deque

def solution(cacheSize, cities):

    answer = 0

    cache = deque([])

    for city in cities:
        
        ### 도시이름의 대소문자를 구분하지 않음
        city = city.lower()

        if cacheSize == 0:
            answer += 5

        else:
            if city not in cache:

                ### 정해진 캐시사이즈만큼 도시를 캐시에 입력
                if len(cache) < cacheSize:
                    cache.append(city)
                    answer += 5
                
                ### 캐시가 꽉 차면 가장 예전의 것을 지우고 새로운 것을 입력
                else:
                    cache.popleft()
                    cache.append(city)
                    answer += 5

            ### 캐시에 이미 도시가 있다면 순서를 갱신
            else:
                cache.remove(city)
                cache.append(city)
                answer += 1

    return answer


if __name__ == '__main__':

    ### test case
    cacheSize = 2
    cities = ["Jeju", "Pangyo", "NewYork", "newyork"]

    print(solution(cacheSize, cities))