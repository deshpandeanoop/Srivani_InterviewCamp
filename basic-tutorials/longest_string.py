import numpy as np
def find_unique_strings(s):
    start = 0
    end = 0
    check_str = ""
    A = np.array([])
    for i in range(0, len(s)):
        if s[i] in check_str:
            A = np.append(A, np.array([check_str]))
            while s[i] in check_str:
                check_str = check_str.replace(check_str[0],"")
                A = np.append(A, np.array([check_str]))
            check_str += s[i]
            start += 1
        else:
            if check_str != "":
                A = np.append(A, np.array([check_str]))
            check_str += s[i]
            while end < len(s)-1:
                end += 1
    return A

def find_longest_string(A):
    length = len(A[0])
    longest_string = A[0]
    for i in A:
        if len(i) > length:
            length = len(i)
            longest_string = i
    return longest_string

if __name__ == "__main__":
    s = "whatwhywhere"
    A = find_unique_strings(s)
    s = find_longest_string(A)
    print(s)