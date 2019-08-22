###
#小Q开了一家冰淇林店，他要用n种配料制作一个冰淇淋。目前每种配料在店里有存货wi份，如果用完了要去买，每种配料一份价格为vi元。小Q现在准备了一些钱，他最多能做出多少分冰淇淋呢？
#输入第一行为配料数量n和钱数m，第二行有n个数字，为每种材料的存货wi；第三行有n个数字为vi
###
# while True:
#     try:
#         n, m = list(map(int, input().split()))
#         kind = list(map(int, input().split()))#wi
#         price = list(map(int, input().split()))#vi
#         per = 0
#         restPrice = m
#         count = 0 # result
#         c = list(zip(kind,price))
#         c.sort()
#         kind[:],price[:] = zip(*c)# sort by kind(wi)
#         current = 0
#         while kind[-1] != 0:
#             if kind[current] == 0: continue
#             minKind = kind[current]
#             count += minKind
#             for index, item in enumerate(kind): kind[index] -= minKind
#             if kind[-1] == 0: break
#             for index, item in enumerate(kind):
#                 if item == 0:
#                     if price[index] <= restPrice:
#                         kind[index] += 1
#                         restPrice = restPrice - price[index]
#                         # print(restPrice)
#             if 0 in kind or restPrice < min(price):
#                 break
#             else:
#                 continue
#         for item in price:
#             per += item
#         count += int(restPrice / per)
#         print(count)

#     except:
#         break

import math
low, high = list(map(int, input().split()))
bit10, bit0 = 0, 0
flag = 1
for i in range(low, high):
    flag = 1
    if i <= 3 and i > 1:
        bit0 += i
        continue
    if i % 6 != 1 and i % 6 != 5:
        continue
    sq = int(math.sqrt(i))
    for j in range(5, sq + 1, 6):
        if i % j == 0 or i %(j + 2) == 0:
            flag = 0
    if flag == 1:
        if i < 10: bit0 += i
        else:
            num = list(map(int, str(i)))
            bit0 += num[-1]
            bit10 += num[-2]
print(min(bit0, bit10))

# num = input().split()
# result = []
# if int(num[0], 16) != len(num) or int(num[0], 16) >= 127:
#     exit()
# for i in range(1, len(num)):
#     ii = num[i]
#     A = hex(int(ii, 16))
#     if A == '0xa':
#         result.append('12')
#         result.append('34')
#     elif A == '0xb':
#         result.append('AB')
#         result.append('CD')
#     else:
#         B = str(A)
#         result.append(B[2:])
# x = len(result) + 1
# x = str(hex(x))
# print(x[2:], end = ' ')
# for i in result:
#     print(str(i), end = ' ')
    