def find_minimum(A, mid, closest_element, target):
    if closest_element == None or abs(A[mid]-target)<abs(A[closest_element]- target):
        closest_element = mid
    return closest_element  

def find_the_closest_element(A, target):
    start = 0
    end = len(A)-1
    closest_element = None
    while(start<=end):
        mid = start+(end-start)//2
        closest_element = find_minimum(A,mid,closest_element, target)
        if A[mid] > target:
            end = mid - 1
        elif A[mid] < target:
            start = mid + 1
        elif A[mid] == target:
            return mid
    return closest_element
        


if __name__ == "__main__":
    A=[10,20,30,40,50]
    target = 23
    closest_element = find_the_closest_element(A,target)
    print(A[closest_element])
