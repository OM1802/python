def main():
    number=getnum()
    meow(number)
    
def getnum():
    while True:
        n=int(input("ENTER VALUE: "))
        if n>0:
            return n

def meow(n):
    for _ in range(n):
        print("meow \n", end="")
        
main()
