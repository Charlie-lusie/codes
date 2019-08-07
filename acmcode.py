while 1:
    number = list(map(int, input().split()))
    if number == "" or len(number) == 0:
        break;
    else:
        kk = number[0]
    init = 2
    count, t = 0, 0
    flag = 1
    while 1:
        for j in range(0, t):
            init += 1
            #print(init, '\n')
            count += 1
            if count >= kk:
                flag = 0
                break
        if (flag ==0):
            print(init)
            break
        init -= 1
        t += 1
        count += 1
        if count >= kk:
            print(init) 
            break


