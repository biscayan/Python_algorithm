import collections

# solution 1, using dictionary, 64 ms
def numJewelsInStones(jewels: str, stones: str) -> int:
        answer = 0
        stone_dict = {}

        for stone in stones:
            if stone in stone_dict:
                stone_dict[stone] += 1
            else:
                stone_dict[stone] = 1

        for jewel in jewels:
            if jewel in stone_dict:
                answer += stone_dict[jewel]

        return answer

# solution 2, using defaultdict, 32 ms
def numJewelsInStones(jewels: str, stones: str) -> int:
    answer = 0
    stone_dict = collections.defaultdict(int)

    for stone in stones:
        stone_dict[stone] += 1

    for jewel in jewels:
        answer += stone_dict[jewel]

    return answer

# solution 3, using Counter, 60 ms
def numJewelsInStones(jewels: str, stones: str) -> int:
    answer = 0
    stone_count = collections.Counter(stones)

    for jewel in jewels:
        answer += stone_count[jewel]

    return answer