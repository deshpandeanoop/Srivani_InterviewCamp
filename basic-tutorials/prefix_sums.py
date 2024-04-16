
def find_indices(A):
    sum = 0
    sum_map = {}
    index_map = {}
    for i in range(0,len(A)-1):
        sum += A[i]
        if sum == 0:
           index_map[0] = i
        for j in sum_map.keys():
            if j == sum:
                index_map[j+1] = i
        sum_map[sum] = i
    return index_map

if __name__ == "__main__":
    A = [-1,2,1,-4,2,3,-1,2]
    index_map = find_indices(A)
    for j in index_map.keys():
        print(j,index_map[j])