#Code for Selection Sorting algorithm for lists

def selection_sort(l):
    n=len(l)
    for i in range(n-1):
        min_index=i
        for j in range(i+1, n):
            if l[j]<l[min_index]:
                min_index=j
        l[i],l[min_index]=l[min_index],l[i]
    return l
    
list=[20,14,50,89,100,1,91,14,0o3,45]
print(selection_sort(list))
