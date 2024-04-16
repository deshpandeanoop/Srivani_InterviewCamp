def find_fibonacci(n):
    #while n>0:
        print(n)
        if n == 1 or n == 2:
            return 1
        else:
            return find_fibonacci(n-1)+find_fibonacci(n-2)

if __name__ == "__main__":
    n = find_fibonacci(5)
    print(n)