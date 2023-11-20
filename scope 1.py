
# the value of x are different baed on the value that will print in main function
num = 5
def main():
    print(func1(2), func2(1))

def func1(x):
    num = 5
    return x*num
def func2(x):
    i = 4
    y = 3
    return i*x+y-num

main()