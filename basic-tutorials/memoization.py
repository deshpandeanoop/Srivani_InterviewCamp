def find_fibonacci(n, dict):
    if n==1 or n==2:
        return 1
    if n in dict.keys():
        return dict[n]
    result= find_fibonacci(n-1, dict)+find_fibonacci(n-2, dict)
    dict[n] = result
    return result

if __name__ == "__main__":
    dict = {}
    n = find_fibonacci(5, dict)
    print(n)