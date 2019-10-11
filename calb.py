def solver(a, b):
    low, high = 0, a
    mid = (low + high) / 2
    while round(mid ** b, 6) != a:
        if mid ** b > a:
            high = mid
        elif mid ** b < a:
            low = mid
        mid = (low + high) / 2
    return mid

if __name__ == "__main__":
    res = solver(1000, 2)