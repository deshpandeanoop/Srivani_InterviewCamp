def calculate_power(x,y): 
    exp = y
    if abs(exp) == 1:
        power = x
    else:
        power = calculate_power(x,abs(exp)-1)*calculate_power(x,1)
    if y<0:
        return 1/power
    else:
        return power
if __name__ == "__main__":
    x = 2
    y = -1
    n = calculate_power(x,y)
    print(n)