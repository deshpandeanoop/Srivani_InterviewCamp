def find_peak(A):
    start = 0
    end = len(A)-1
    while(start<=end):
        mid = start + (end-start)//2
        if (mid == len(A)-1 and A[mid-1] < A[mid]) or (mid == 0 and A[mid+1] < A[mid]):
            return mid
        if A[mid-1] < A[mid] and A[mid+1] > A[mid]:
            start = mid + 1
        elif A[mid-1] > A[mid] and A[mid+1] < A[mid]:
            end = mid - 1
        elif A[mid-1] < A[mid] and A[mid+1] < A[mid]:
            return A[mid]
        elif A[mid-1] > A[mid] and A[mid+1] > A[mid]:
            if A[mid-1] > A[mid+1]:
                end = A[mid-1]
            else:
                start = mid + 1
     
if __name__=="__main__":
    A = [3,2,4]
    peak = find_peak(A)
    print(peak)