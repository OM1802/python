#code for insrtion sorting algorithm implemented on an unsorted list

def insertion_sort(l):
    n=len(l)
    for i in range(1,n):
        key=l[i]
        j=i-1
        while j>=0 and key<l[j]:
            l[j+1]=l[j]
            j-=1
        l[j+1]=key
    return l
        
list=[20,14,58,1,9,14,99,25,2]
print(insertion_sort(list))
