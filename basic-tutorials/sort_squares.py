import numpy as np

def sort_array(B):
    start = len(B)-1
    while(start>0):
        if(B[start] < B[start-1]):
            temp = B[start]
            B[start] = B[start-1]
            B[start-1] = temp
        start -= 1
    return B

def sort_squares(A):
    B = np.array([])
    for i in range(0,len(A)):
        square = int(A[i]*A[i])
        B = np.append(B, np.array([square]))
        if i>0 and i<len(A):
            B = sort_array(B)
    return B

if __name__ == "__main__":
    A = [-4,-2,-1,0,3,5]
    A = sort_squares(A)
    print(A)