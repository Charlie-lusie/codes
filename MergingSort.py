def Merge(SR, TR, i, m, n):
    j, k = m + 1, i
    while(i <=m and j <= n):
        if (SR[i] < SR[j]): 
            TR[k] = SR[i]
            i += 1
        else:
            TR[k] = SR[j]
            j += 1
        k += 1
    if (i <= m):
        for s in range(0, m - i + 1):
            TR[k + s] = SR[i + s]
    if (j <= n):
        for s in range(0, n - j + 1):
            TR[k + s] = SR[j + s]
    return TR

def MSort(SR, TR1, s, t):
    if (s == t):
        TR1[s] = SR[s]
    else:
        m = int((s + t) / 2)
        TR2 = []
        for i in range(0, len(SR)):
            TR2.append(0)
        TR2 = MSort(SR, TR2, s, m)
        TR2 = MSort(SR, TR2, m + 1, t)
        TR1 = Merge(TR2, TR1, s, m ,t)
    return TR1

def MergeSort(L):
    return MSort(L, L, 0, len(L) - 1)

print(MergeSort([3, 1, 4, -1, 2, 4, 8]))

