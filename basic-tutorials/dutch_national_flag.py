def swap(A,i, boundary):
    temp = A[i]
    A[i] = A[boundary]
    A[boundary] = temp
    return A

def partition_into_three(A):
    low_boundary = 0
    high_boundary = len(A)-1
    i =0
    while(i < high_boundary):
        if A[i] < pivot:
            swap(A, i, low_boundary)
            low_boundary += 1
            i += 1
        elif A[i] > pivot:
            swap(A, i, high_boundary)
            high_boundary -= 1
        else:
            i += 1
    return A
        
if __name__ == "__main__":
    A = [3,2,1,4,3,6,7,5]
    pivot = 4
    A = partition_into_three(A)
    print(A)