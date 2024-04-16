def swap(A, start, end):
    temp = A[start]
    A[start] = A[end]
    A[end] = temp
    return A

def reverse_the_array(A):
    start = 0
    end = len(A) - 1
    while(start<end):
        swap(A,start,end)
        start += 1
        end -= 1
    return A

if __name__ == "__main__":
    A = [1,2,3,4,5]
    A = reverse_the_array(A)
    print(A)