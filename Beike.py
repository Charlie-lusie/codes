def AddDict(key):
    global md
    if key in md:
        value = md[key] + 1
        if value > 1:
            md[key] = 0
            AddDict(key + 1)
        else:
            md[key] = value
    else:
        md[key] = 1

md = {}
n = list(map(int, input().split()))
N = n[0]
if N <= 0 or N > 10**6: exit()
wi = list(map(int, input().split()))
if len(wi) != N: exit()
for i in range(N):
    AddDict(wi[i] + 1)
count = 0
for k, v in md.items():
    if v == 1:
        count += 1
print(count)