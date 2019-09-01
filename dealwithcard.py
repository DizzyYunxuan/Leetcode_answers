def Solution(s, m, b): 
    res = []
    solver(s, m, b, '', '', res)
    return res

def solver(s, m, b, choosepath, newseq, res):
    if newseq == b:
        res.append(choosepath)
        return
    elif len(m) == 0:
        return
    else:
        for i in 'dlr':
            if i == 'd':
                solver(s-1, m[1:], b, choosepath+i+' ', newseq, res)
            elif i == 'l':
                solver(s-1, m[1:], b, choosepath+i+' ', m[0]+newseq, res)
            else:
                solver(s-1, m[1:], b, choosepath+i+' ', newseq+m[0], res)

if __name__ == "__main__":
    res = Solution(3, '123', '3')