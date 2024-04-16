def find_subarray_with_sum(A, target_sum):
    sum = 0
    sum_map ={}
    index_map = {}
    for i in range(0, len(A)):
        sum += A[i]
        sum_map[sum] = i
        if sum == target_sum:
            index_map[0] = i
        if sum>target_sum:
            if sum-target_sum in sum_map.keys():
                index_map[sum_map[sum-target_sum]+1] = i
    return index_map

if __name__ == "__main__":
    A = [2,4,-2,1,-3,5,-3]
    target_sum = 5
    index_map = find_subarray_with_sum(A, target_sum)
    for j in index_map.keys():
        print(j,index_map[j])