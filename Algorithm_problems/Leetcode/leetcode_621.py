from collections import Counter

def leastInterval(tasks, n) -> int:
    counts = list(Counter(tasks).values())
    max_count = max(counts)
    max_count_tasks = counts.count(max_count)
    num_of_chunks_with_idles = max_count-1
    len_of_a_chunk_with_idle = n+1
    len_of_all_chunks = num_of_chunks_with_idles * len_of_a_chunk_with_idle + max_count_tasks
    return max(len(tasks), len_of_all_chunks)