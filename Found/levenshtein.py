# -*- coding: utf8 -*-


def lev(s1, s2):
    if not s1:
        return len(s2)
    elif not s2:
        return len(s1)
    mtx = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    for i in range(1, len(s1) + 1):
        mtx[i][0] = i
    for j in range(1, len(s2) + 1):
        mtx[0][j] = j
    for j in range(1, len(s2) + 1):
        for i in range(1, len(s1) + 1):
            if s1[i - 1] == s2[j - 1]:
                mtx[i][j] = mtx[i - 1][j - 1]
            else:
                mtx[i][j] = 1 + min(mtx[i][j - 1],
                                    mtx[i - 1][j],
                                    mtx[i - 1][j - 1])
    return mtx[-1][-1]


print(lev('abcdef', 'abc'))
