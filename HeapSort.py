def HeapAdjust(H,s,m):#H[s…m]中除了s位置都满足堆的定义，函数就是为了调整s
    rc = H[s]
    j = 2*s
    while(j<=m):
        if (j<m and H[j] < H[j + 1]): j += 1#j应该为值较大的那个
        if (rc >= H[j]): break
        H[s] = H[j]
        s = j
        j *= 2
    H[s] = rc
    return H

def HeapSort(H):
    #H = [-1] + H
    for i in range(int(len(H)/2), -1, -1):
        H = HeapAdjust(H, i, len(H) - 1)
    for i in range(len(H) - 1, 0, -1):
        H[0], H[i] = H[i], H[0]
        H = HeapAdjust(H, 0, i-1)
    return H

print(HeapSort([1,4,2,6,0,2,5]))
print(HeapSort([1,3, -1,2,61,1,0,0,5]))