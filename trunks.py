def get_min_boxes(things,box_weight):
    things=sorted(things,reverse=True)#将数据由大到小排序
    print(things)
    m=len(things)-1;count=0
    for i in range(len(things)):
        sum=0
        print('{',end='')
        sum=things[i]
        print(things[i],' ',end='')
        while m>=0:
            j=m
            sum+=things[j]
            if sum>box_weight:
                count+=1
                break
            # print(things[j],'',end='')
            m-=1
        if j==i:
            # count+=1
            # print('}')
            break
        # print('}')
    # print('最少需要使用',count,'个容积为',box_weight,'的箱子')
    return count
if __name__=='__main__':
    things=[4,8,1,4,2,1]
    things=[1,2]
    box_weight=3
    # things=[3,15,14,19,13,4,10,4,20,3,1,7,13,8,18,18,20,5,9,8]
    # box_weight=20
    res = get_min_boxes(things,box_weight)
    x = 1
