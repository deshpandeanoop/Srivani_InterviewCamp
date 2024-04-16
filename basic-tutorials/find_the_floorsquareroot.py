def find_floor_square_root(X):
    start = 0
    end = X//2
    if X == 0:
        return 0
    if X == 1:
        return 1
    while(start<=end):
        mid = start+(end-start)//2
        if mid*mid > X:
            if (mid - 1)*(mid - 1) < X:
                return mid - 1
            else:
                end = mid - 1
        elif mid*mid < X:
            start = mid + 1
            if mid == end:
                return mid
        else:
            return mid

if __name__=="__main__":
    X = 8
    square_root = find_floor_square_root(X)
    print(square_root)

