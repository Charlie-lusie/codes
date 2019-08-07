def basic_solution(total, w, v):
    item_num = len(w)  # item_num 个物品，至多放 item_num 次
    # dp[尝试放入i][背包容量j]
    dp = [[0 for _1 in range(total + 1)] for _2 in range(item_num + 1)]  # which is : int dp[item_num+1][total+1] = {0}
    trace = [[[] for _1 in range(total + 1)] for _2 in range(item_num + 1)]  # 放入背包中的物品的最优组合的序号list
    for i in range(item_num):  # 尝试放入第i个物品(物品序号从0起||显然，尝试次数从1起,即i+1)
        for j in range(total, -1, -1):  # form $total to $0, step=-1  # 背包可用容量
            if j >= w[i] and dp[i][j - w[i]] + v[i] > dp[i][j]:  # 尝试放入时选择放入第[i]个物品
                dp[i + 1][j] = dp[i][j - w[i]] + v[i]  # 更新第i+1次尝试放入的推测值
                trace[i + 1][j] = trace[i][int(j - w[i])] + [i]
            else:  # 跳过物品，拷贝"前[i]次尝试放入"的堆栈数据到[i+1]上, 事实上可以直接放弃拷贝过程节省程序开销
                dp[i + 1][j] = dp[i][j]
                trace[i + 1][j] = trace[i][j]
    return {
        "max_value": dp[item_num][total],
        "package_trace": trace[item_num][total]
    }

def basic_solution2(total, w, v):
    item_num = len(w)  # item_num 个物品，至多放 item_num 次
    # dp[尝试放入i][背包容量j]
    dp = [0 for _1 in range(total + 1)]
    trace = [[] for _1 in range(total + 1)]  # 放入背包中的物品的最优组合的序号list
    for i in range(item_num):  # 尝试放入第i个物品(物品序号从0起||显然，尝试次数从1起,即i+1)
        for j in range(total, -1, -1):  # form $total to $0, step=-1  # 背包可用容量
            if j >= w[i] and dp[j - w[i]] + v[i] > dp[j]:  # 尝试放入时选择放入第[i]个物品
                dp[j] = dp[j - w[i]] + v[i]  # 更新第i+1次尝试放入的推测值
                trace[j] = trace[int(j - w[i])] + [i]
    return {
        "max_value": dp[total],
        "package_trace": trace[total]
    }

def basic_solution3(total, w, v):
    item_num = len(w)  # item_num 个物品，至多放 item_num 次
    # dp[尝试放入i][背包容量j]
    dp = [0 for _1 in range(total + 1)]
    trace = [[] for _1 in range(total + 1)]  # 放入背包中的物品的最优组合的序号list
    for i in range(item_num):  # 尝试放入第i个物品(物品序号从0起||显然，尝试次数从1起,即i+1)
        lower = max(total - sum(w[i:]), w[i])
        for j in range(total, lower - 1, -1):  # form $total to $0, step=-1  # 背包可用容量        
            if  dp[j - w[i]] + v[i] > dp[j]:  # 尝试放入时选择放入第[i]个物品
                dp[j] = dp[j - w[i]] + v[i]  # 更新第i+1次尝试放入的推测值
                trace[j] = trace[int(j - w[i])] + [i]
    return {
        "max_value": dp[total],
        "package_trace": trace[total]
    }

def basic_solution4(total, w, v):
    item_num = len(w)  # item_num 个物品，至多放 item_num 次
    # dp[尝试放入i][背包容量j]
    dp = [float("-inf") for _1 in range(total + 1)]
    dp[0] = 0
    trace = [[] for _1 in range(total + 1)]  # 放入背包中的物品的最优组合的序号list
    for i in range(item_num):  # 尝试放入第i个物品(物品序号从0起||显然，尝试次数从1起,即i+1)
        lower = max(total - sum(w[i:]), w[i])
        for j in range(total, lower - 1, -1):  # form $total to $0, step=-1  # 背包可用容量        
            if  dp[j - w[i]] + v[i] > dp[j]:  # 尝试放入时选择放入第[i]个物品
                dp[j] = dp[j - w[i]] + v[i]  # 更新第i+1次尝试放入的推测值
                trace[j] = trace[int(j - w[i])] + [i]
    return {
        "max_value": dp[total],
        "package_trace": trace[total]
    }

total = 8
w = [2, 4, 6, 3]
v = [10, 20, 21, 15]
print(basic_solution3(total, w, v))
print(basic_solution4(total, w, v))