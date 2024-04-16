def place_target_with_bs(A, target):
    start = 0
    end = len(A) - 1
    mid = 0
    '''if A[end] <= target:
            return end+1
    if A[start] > target:
            return 0
    while(start <= end):
        mid = start + (end - start)//2
    if mid == end and A[mid-1] < target:
            return end
        if A[mid] > target:
            if A[mid-1] < target:
                 return mid
            else:
                end = mid - 1
        if A[mid] < target:
            start = mid + 1
        if A[mid] == target:
            if A[mid+1] > target:
                return mid+1
            else:
                start = mid+1'''
    while start <= end:
        mid = start + (end - start)//2
        if A[mid] <= target:
            if mid == len(A)-1:
                return len(A)
            else:
                start = mid +1
        else:
            if mid == 0 or A[mid-1] <= target:
                return mid
            else:
                end = mid - 1
         
    return -1


if __name__ == "__main__":
    A = [2,2,2,2,2]
    target = 2
    index = place_target_with_bs(A, target)
    if index != -1:
        print(index)