def findContentChildren(g, s):
    answer = 0
    g_idx, s_idx = 0, 0
    g.sort()
    s.sort()
    while g_idx < len(g) and s_idx < len(s):
        if g[g_idx] <= s[s_idx]:
            answer += 1
            g_idx += 1
        s_idx += 1
    return answer