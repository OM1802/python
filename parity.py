def main():
    x=int(input("ENTER VALUE: "))
    if parity(x):
        print("EVEN")
    else:
        print("ODD")
        
def parity(n):
    return True if n%2==0 else False
    
main()
