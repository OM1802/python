#Bubble sorting algorithm for list in python

def bubble_sort(l):
    n=len(l)
    for i in range(n):
        for j in range(0, n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l
    
list=[25,14,80,12,2,19,85,73,1]
print(bubble_sort(list))


#Optimized Bubble sorting algorithm for list in python

def optimized_bubble_sort(l):
    n=len(l)
    swapped=False
    for i in range(n):
        for j in range(0, n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
                swapped=True
        if not swapped:
            break
    return l
    
list=[25,14,80,12,2,19,85,73,1]
print(optimized_bubble_sort(list))

