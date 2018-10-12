# -*- coding: utf8 -*-


def levenshtein(s1, s2):
    m, n = len(s1), len(s2)
    if m == 0:
        return n
    if n == 0:
        return m
    mtx = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        mtx[i][0] = i
    for j in range(1, n + 1):
        mtx[0][j] = j
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                mtx[i][j] = mtx[i - 1][j - 1]
            else:
                mtx[i][j] = min(mtx[i - 1][j] + 1,
                                mtx[i][j - 1] + 1,
                                mtx[i - 1][j - 1] + 1)
    return mtx[m][n]


print(levenshtein('abcdef', 'abc'))
