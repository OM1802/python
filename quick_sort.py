#Python code implementing quick sort algorithm on an unsorted list

def quick_sort(l):
    if len(l)<=1:
        return l
    else:
        pivot=l[0]
        left=[x for x in l[1:] if x<=pivot]
        right=[x for x in l[1:] if x>pivot]
        return quick_sort(left)+[pivot]+quick_sort(right)
        
list=[25,14,10,1,25,100,14,36,3]
print(quick_sort(list))
