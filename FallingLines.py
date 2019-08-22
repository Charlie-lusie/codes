def FindLine(y, Left, Right):
    if len(y) == 0: return None
    if len(y) != len(Left): return None
    result = []
    while len(y) != 0:
        idx = y.index(min(y))
        this_l, this_r = Left[idx], Right[idx]
        Judge(result, this_l, this_r)
        del y[idx]
        del Left[idx]
        del Right[idx]
    true_result = []
    for i in range(len(result)):
        if result[i][2] == 0:
            true_result.append([result[i][0], result[i][1]])
    return true_result

def Judge(result, this_l, this_r):
    if len(result) == 0:
        result.append([this_l, this_r, 0])
        return
    for i in range(len(result)):
        if this_r <= result[i][0]:#能到这一步说明上一轮一定在之前那个线段的右侧，这里又判断在左侧，说明必定在两个线段中间的部分
            insert_position = i
            result.insert(insert_position, [this_l, this_r, 0])
            return
        elif this_l < result[i][1]: # not beyond right, overlap happends
            if this_l < result[i][0]: result.insert(i,[this_l, result[i][0], 1])#有重叠，给上面线段多出来一截赋label=1，表示这一部分已经存在线段，后续在此范围内的线段不能放进来
            if this_r > result[i][1]: result.insert(i,[result[i][1], this_r, 1])
            return
    result.append([this_l, this_r, 0])
    return

print(FindLine([1, 2, 3, 1.5, 2.5], [1, 1.8, 2, 4, 3], [2, 3, 2.5, 5, 5.5]))#线段高度y，左右顶点
