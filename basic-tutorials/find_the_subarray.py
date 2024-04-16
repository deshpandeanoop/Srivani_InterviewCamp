import numpy as np

def find_the_subarray(A):
    start = 0
    end = len(A)-1
    i = start
    while i<len(A):
        for j in range(start+1,len(A)):
            if A[i] > A[j]:
                start = i
                i = len(A)
                break
        i += 1
    i = end
    while j > 0:
        for j in range(end-1,-1,-1):
            if A[i] < A[j]:
                end = i
                i = 0
                break
        i -= 1
    B = np.array([])
    i = start
    while i < (end-start+1):
        B = np.append(B,np.array([A[i]]))
        i += 1
    return B
        
if __name__ == "__main__":
    A = [0,2,3,1,8,6,9]
    A = find_the_subarray(A)
    print(A)