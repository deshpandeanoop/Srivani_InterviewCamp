import numpy as np
def get_sub_array(A, target):
    start = 0
    end = 0
    sum = A[0]
    B = np.array([])
    while(end < len(A)-1):
        if(start > end):
            end = start
            sum = A[start]
        if sum < target:
            if end >= len(A):
                break
            end += 1
            sum += A[end]
        elif sum > target:
            sum -= A[start]
            start += 1
        elif sum == target:
            B = np.append(B, np.array([start]))
            B = np.append(B, np.array([end]))
            break
    return B
            
        
if __name__ == "__main__":
    A = [5,3,1,7,6,8,9]
    target = 14
    A = get_sub_array(A, target)
    print(int(A[0]), int(A[1]))