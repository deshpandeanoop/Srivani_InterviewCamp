def find_min_in_cyclic_arr(A):
    start = 0
    end = len(A)-1
    right_most = A[-1]
    while(start<=end):
        mid = start + (end-start)//2
        if (A[mid] <= right_most) and (mid == 0 or A[mid-1]>A[mid]):
            return mid
        elif A[mid] > right_most:
            start = mid + 1
        else:
            end = mid - 1
    return -1

if __name__ == "__main__":
    A = [7,8,1,2,3,4]
    min = find_min_in_cyclic_arr(A)
    if min != -1:
        print(A[min])