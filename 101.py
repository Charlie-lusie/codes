def FindNDegree(All, conject, current_user, n_degree, weight, result):
    if n_degree == 1:
        for i in range(len(conject)):
            if conject[current_user][i] != 0 and i != All[0]:
                label = 0
                for k in range(0, len(All) - 1):
                    if conject[i][All[k]] != 0:
                        label = 1
                        break
                if label == 0:
                    result.append([i, weight + conject[current_user][i]])
        return
    else:
        for i in range(len(conject)):
            if conject[current_user][i] != 0 and i != All[0]:
                label = 0
                for k in range(0, len(All) - 1):
                    if conject[i][All[k]] != 0:
                        label = 1
                        break
                if label == 0:
                    FindNDegree(All + [i], conject, i, n_degree - 1, weight + conject[current_user][i], result)
    return

def MySort(result):
    id = []
    de = []
    for i in range(len(result)):
        id.append(result[i][0])
        de.append(result[i][1])
    c = list(zip(id,de))
    c.sort()
    id[:],de[:] = zip(*c)
    print(id)
    print(de)
    # sort by de
    for i in range(len(id)):
        for j in range(len(id) -1, i, -1):
            if de[j] > de[j - 1]:
                de[j], de[j - 1] = de[j -1], de[j]
                id[j], id[j -1]  = id[j -1], id[j]
    print(id)


#T = list(map(int, input().split()[0]))
T = [1]
for i in range(T[0]):
    #line1 = list(map(int, input().split()))
    #line2 = list(map(int, input().split()))
    line1 = [10, 5, 2]
    line2 = [13, 0, 3, 5, 0, 4, 9, 0, 6, 8, 0, 7, 5, 1, 2, 6, 1, 6, 3, 2, 9, 7, 3, 4, 3, 3, 5, 3, 3, 8, 3, 3, 9, 3, 5, 8, 9, 7, 8, 9]
    user_num, current_user, n_degree = line1[0], line1[1], line1[2]
    if n_degree < 1 or n_degree > 10:
        print("-1")
        break
    conject = [[0 for _i in range(user_num)] for _j in range(user_num)]
    k = line2[0]
    for j in range(1, 3*k, 3):
        conject[line2[j]][line2[j + 1]] = line2[j+2]
        conject[line2[j + 1]][line2[j]] = line2[j+2]

    result = []
    FindNDegree([current_user], conject, current_user, n_degree, 0, result)
    MySort(result)