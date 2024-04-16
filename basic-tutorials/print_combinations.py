import numpy as np
def print_combos(a, buffer, start_index, buffer_index):
    if buffer_index == len(buffer):
        print(buffer)
        return
    if start_index == len(a):
        return
    for i in range(start_index, len(a)):
        buffer[buffer_index] = a[i]
        print_combos(a, buffer, i+1, buffer_index+1)

if __name__ == "__main__":
    A = [1,2,3,4,5,6]
    B = np.empty(5)
    start_index = 0
    buffer_index = 0
    print_combos(A, B, start_index, buffer_index )
