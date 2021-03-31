import random
def calc(N, CS):
    """
    :param N:  表示小球的颜色数量
    :param CS: 表示每一种颜色的小球数量
    :return: 随机抓取的小球颜色编号
    """
    # 计算小球总数
    dsum = sum(CS)
 
    # 存储每种颜色的小球的概率
    ps = [0]
    for i in range(N):
        ps.append(CS[i]/dsum)
 
    # 按照概率划分区间
    dct = {}
    tmp = 0
    for i in range(N):
        ps[i+1] += ps[i]
        dct[(ps[i], ps[i+1])] = i
 
    tn = random.random()
    print('random int: ', tn)
    rst = 0
    for ky in dct.keys():
        if ky[0] <= tn < ky[1]:
            break
        rst += 1
    print('number of colors: ', rst)
    return rst

calc(3, [1,2,3])