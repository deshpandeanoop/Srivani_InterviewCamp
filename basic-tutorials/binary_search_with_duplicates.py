def binary_search_with_duplicates(A, target):
    start = 0
    end = len(A)-1
    mid = 0
    while(start <= end):
        mid = start + (end - start)//2
        if ((A[mid] > target) or (A[mid] == target and mid > 0 and A[mid-1] == target)):
            end = mid -1
        elif A[mid] < target:
            start = mid + 1
        elif A[mid] == target:
            return mid
    return -1

if __name__ == "__main__":
    A = [1,3,3,3,4,5]
    target = 3
    index = binary_search_with_duplicates(A, target)
    if index != -1:
        print(index)