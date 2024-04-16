
def count_even_numbers(A):
    count = 0
    for i in A:
        if i%2 == 0:
            count += 1
    return count

def get_template_array(A,count):
    B = [-1]*(len(A)+count)
    for i in range(0,len(A)):
        B[i] = A[i]
    for i in range(len(A),count):
        B[i] = -1
    return B

def clone_array(B):
    last_index = -1
    for i in range(len(B)-1,-1,-1):
        if B[i] > -1:
            if B[i]%2 == 0:
                B[last_index] = B[i]
                B[last_index-1] = B[i]
                last_index -= 2
            else:
                B[last_index] = B[i]
                last_index -= 1      
    return B

def clone_even_numbers(A):
    count = count_even_numbers(A)
    B = get_template_array(A,count)
    cloned_array = clone_array(B)
    return cloned_array


if __name__ == "__main__":
    A = [2,4,1,0,3]
    print(A)
    cloned_array = clone_even_numbers(A)
    print(cloned_array)

