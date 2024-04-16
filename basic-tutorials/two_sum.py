import numpy as np

def find_two_sum(A, expected_sum):
    B = np.array([])
    start =0
    end = len(A)-1
    while(start < end):
        if A[start]+A[end] == expected_sum:
            B = np.append(B, np.array([start, end]))
            break
        elif A[start]+A[end] < expected_sum:
            start += 1
        elif A[start]+A[end] > expected_sum:
            end -= 1
    return B

if __name__ == "__main__":
    A = [1,2,3,4,5]
    expected_sum = 8
    B = find_two_sum(A, expected_sum)
    print(str(int(B[0]))+","+str(int(B[1])))