def swap(A, i , boundary):
    temp = A[boundary]
    A[boundary] = A[i]
    A[i] = temp
    return A

def move_zeroes_to_beginning(A):
    boundary = 0
    for i in range(boundary+1,len(A)):
        if A[i] == 0:
            A = swap(A, i, boundary)
            boundary += 1
    return A
            
if __name__ == "__main__":
    A = [2,1,0,3,1,0,0]
    A = move_zeroes_to_beginning(A)
    print(A)