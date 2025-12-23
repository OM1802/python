#Python program implementing merge sort algorithm in an unsorted list

def merge_sort(list):
    if len(list)>1:
        midvalue=len(list)//2
        leftlist=list[:midvalue]
        rightlist=list[midvalue:]
        merge_sort(leftlist)
        merge_sort(rightlist)
    
        i=j=k=0
    
        while i<len(leftlist) and j<len(rightlist):
            if leftlist[i]<rightlist[j]:
                list[k]=leftlist[i]
                i+=1
            else:
                list[k]=rightlist[j]
                j+=1
            k+=1
        
        while i<len(leftlist):
            list[k]=leftlist[i]
            i+=1
            k+=1
        while j<len(rightlist):
            list[k]=rightlist[j]
            j+=1
            k+=1
        
    return list
    
l=[20,10,45,68,1,2,6,4,14,55,47]
print(merge_sort(l))
