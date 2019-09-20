def solution(l):
    l.sort()
    res = 0
    for i in range(len(l)):
        if l[i] < 0:
            # start, end = None, None
            for j in l[i+1:]:
                if 2*l[i] <= l[j] <= -2*l[i]:
                    res += 1
                if l[j] > -2*l[i]:
                    break
                # if not start and l[j] >2*l[i]:
                #     start = j
                # if not end and l[i] < 2*l[j]:
                #     end = i
                # res += end - start + 1
        else:
            for j in l[i+1:]:
                if -2*l[i] <= l[j] <= 2*l[i]:
                    res += 1
                if l[j] > 2*l[i]:
                    break
    return res
if __name__ == "__main__":
    l = [1,-2, 2]
    res = solution(l)
    print(res)
            # start, end = None, None
            # for j in [i+1:]:
            #     if not start and l[j] > 2*l[i]:
            #         start = j
            #     if not end and l[i] < -2*l[j]:
            #         end = i
            #     res += end - start + 1

