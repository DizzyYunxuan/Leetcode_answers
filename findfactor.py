def solver(num):
    cur = [0] * num
    res = [0] * num
    cur[1], cur[2], res[1], res[2] = 1, 1, 1, 2
    for i in range(3, len(cur)):
        if int((i+1)**(1/2))**2 == i+1:
            cur[i] = cur[int((i+1)**1/2)]*2
            res[i] = res[i-1] + cur[int((i+1)**1/2)]*2
        elif (i+1)%2 == 0:
            cur[i] = cur[1]+cur[(i+1)//2-1]
            res[i] = res[i-1] + cur[1] + cur[(i+1)//2-1]           
        else:
            cur[i] = 1
            res[i] = res[i-1] + 1
    return res[num-1]


if __name__ == "__main__":
    res = []
    # # for i in range(8, 20):  
    #     res.append(solver(i))
    print(solver(14))
    x =1