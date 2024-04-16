def max(a,b):
   if a>b:
      return a
   else:
      return b
   
def get_max_sum(A):
    max_sum = A[0]
    temp_sum = A[0]
    for i in range(1,len(A)-1):
        temp_sum = max(A[i], temp_sum+A[i])
        max_sum = max(max_sum, temp_sum)
    return max_sum

if __name__ == "__main__":
    A = [-2,-3,4,-1,-2,1,5,-1]
    max_sum = get_max_sum(A)
    print(max_sum)