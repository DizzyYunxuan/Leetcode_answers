def distance(x, y):
    return ((x[0] - y[0])**2 + (x[1]-y[1])**2)**(1/2)

# def sintheta(l1, l2):
#     k1 = (l1[0][0] - l1[1][0]) / (l1[0][1] - l1[1][1])
#     k2 = (l2[0][0] - l2[1][0]) / (l2[0][1] - l2[1][1])
#     tantheta = abs(k1-k2)/(1+k1*k2)
#     sintheta = (tantheta**2/(1+tantheta**2)) ** 1/2
#     return sintheta

# def solution(points):
#     a = distance(points[0], points[1])
#     b = distance(points[1], points[2])
#     c = distance(points[2], points[3])
#     d = distance(points[3], points[0])
#     m = distance(points[0], points[2])
#     n = distance(points[1], points[3])

#     sin = sintheta([points[0], points[2]], [points[1], points[3]])

#     sq = 1/2 *m*n*sintheta
def distance(x, y):
    return ((x[0] - y[0])**2 + (x[1]-y[1])**2)**(1/2)

def solution(points):
    leftmost, rightmost, upmost, botmost = float('inf'), -float('inf'), -float('inf'), float('inf')
    lin, rin, upin, botin = 0, 0, 0, 0
    points.sort()
    leftmost = points[0][0]
    i, lin = 0, []
    while points[i][0] == leftmost:
        lin.append(points[i])
        i+=1
    return l1, l2


if __name__ == "__main__":
    points = [
        [50,500],
        [95.3333,500],
        [114.755,265.303],
        [50,234.286],
        [220,500],
        [220,315.714],
        [114.755,265.303],
        [95.3333,500],
        [220,50],
        [132.571,50],
        [114.755,265.303],
        [220,315.714],
        [50,50],
        [50,234.286],
        [114.755,265.303],
        [132.571,50]
    ]
    res = solution(points)