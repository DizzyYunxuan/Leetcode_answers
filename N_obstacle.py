def solution(payload, field, obstacle):
    # horizontal pyload
    for obs in obstacle:# Tranversing every obstacle
        field[obs[0]][obs[1]] = 0 # Set obstacle position to 0
        x_p, y_p = len(payload), len(payload[0])# Get pyload size
        x_start = obs[0] - x_p + 1 # Set area that Anchor of pyload can't be settle.
        x_end = obs[0] +1

        y_start = obs[1] - y_p +1
        y_end = obs[1] + 1
        for i in range(x_start, x_end): # Set all elements in area to 0
            for j in range(y_start, y_end):
                field[i][j] = 0
    
    for obs in obstacle:# vertical pyload
        x_p, y_p = len(payload[0]), len(payload)
        x_start = obs[0] - x_p + 1
        x_end = obs[0] +1

        y_start = obs[1] - y_p +1
        y_end = obs[1] + 1
        for i in range(x_start, x_end):
            for j in range(y_start, y_end):
                field[i][j] = 0
        res = 0
        for i in field:
            res += sum(i)
    
    res = 1 if res != 0 else 0
    return res


if __name__ == '__main__':
    payload = [[1,1],[1,1]]
    field = [[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]
    obstacle = [[2,2],[4,5],[0,0],[1,1],[3,3],[4,4]]
    res = solution(payload, field, obstacle)
    print(res)