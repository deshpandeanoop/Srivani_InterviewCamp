
def swap(A, i, boundary):
    temp = A[i]
    A[i] = A[boundary]
    A[boundary] = temp
    return A

def move_zeroes_to_the_end(A):
    boundary = len(A)-1
    for i in range(len(A)-1,-1,-1):
        if A[i] == 0:
            swap(A,i,boundary)
            boundary -= 1
    return A

if __name__ == "__main__":
    A = [0,1,2,0,1,2]
    A = move_zeroes_to_the_end(A)
    print(A)