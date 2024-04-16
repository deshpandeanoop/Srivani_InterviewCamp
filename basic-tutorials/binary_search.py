def binary_search(A, target):
    start = 0
    end = len(A)-1
    mid = 0
    while(start<=end):
        mid = start+(end-start)//2
        if A[mid] > target:
            end = mid - 1
        elif A[mid] < target:
            start = mid + 1
        elif A[mid] == target:
            return mid
    return -1
        



if __name__ == "__main__":
    A = [1,2,3,4,5]
    target = 6
    index = binary_search(A, target)
    if index != -1:
        print(index)
    else:
        print("not found")