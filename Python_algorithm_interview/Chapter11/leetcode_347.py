from collections import Counter

def topKFrequent(nums, k: int):
    num_list = []
    num_freq = Counter(nums).most_common()
    for i in range(k):
        num_list.append(num_freq[i][0])
    return num_list