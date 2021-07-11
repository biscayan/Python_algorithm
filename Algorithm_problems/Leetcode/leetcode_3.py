def lengthOfLongestSubstring(s: str) -> int:
    answer = 0
    l_idx = 0
    used = {}

    for r_idx, char in enumerate(s):
        if char in used and l_idx <= used[char]:
            l_idx = used[char] + 1
        else:
            answer = max(answer, r_idx-l_idx+1)
        used[char] = r_idx

    return answer