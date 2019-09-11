
d = {}

def solution(space, mem, path, apps):
    if space < 0 or mem < 0:
        return False
    for i in range(len(apps)):
        if solution(space-d[apps[i]])