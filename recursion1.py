def main():
    l=[1,2,3,4,5,6,7,8,9]
    recursion(l)
    
def recursion(x,ind=0):
    if ind==len(x):
        return 0
    else:
        print(x[ind])
        recursion(x,ind=ind+1)

main()
    