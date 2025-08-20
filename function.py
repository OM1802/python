def main():
    n=int(input("ENTER NUMBER: "))
    print(factorial(n))

def factorial(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f 

main()
