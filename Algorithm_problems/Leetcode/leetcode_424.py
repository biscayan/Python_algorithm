from collections import Counter

def characterReplacement(s, k):
    counts = Counter()
    left = right = 0

    for right in range(1, len(s)+1):
        counts[s[right-1]] += 1
        most_char_n = counts.most_common(1)[0][1]

        if right-left-most_char_n > k:
            counts[s[left]] -= 1
            left += 1

    return right - left

s = "ABAB"
k = 2
print(characterReplacement(s, k))