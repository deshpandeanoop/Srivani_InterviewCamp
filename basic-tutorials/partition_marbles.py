from enum import Enum
def swap(A, first, second):
    temp = A[first]
    A[first] = A[second]
    A[second] = temp
    return A
   
'''def partition_marbles(A, pivot):
    start = 0
    end = len(A)-1
    i = 0
    while(i < end):
        if A[i] == pivot+1:
            swap(A, i, start)
            start += 1
            i += 1
        elif A[i] == pivot+2:
            swap(A, i, end)
            end -= 1
        elif A[i] == pivot:
            i += 1
    return A

if __name__ == "__main__":
    A = [1,0,1,2,1,0,1,2] #0 (Red), 1 (White) and 2 (Blue)
    pivot = 0
    A = partition_marbles(A, pivot)
    print(A)'''

class Colour(Enum):
    RED = 1
    WHITE = 0
    BLUE = 2

def partition_marbles(A):
    start = 0
    end = len(A)-1
    colour = 0
    while(colour < end):
        if A[colour] == Colour.RED.value:
            swap(A, colour, start)
            start += 1
            colour += 1
        elif A[colour] == Colour.BLUE.value:
            swap(A, colour, end)
            end -= 1
        elif A[colour] == Colour.WHITE.value:
            colour += 1
    return A

if __name__ == "__main__":
    A = [1,0,1,2,1,0,1,2] #0 (Red), 1 (White) and 2 (Blue)
    pivot = 0
    A = partition_marbles(A)
    print(A)

