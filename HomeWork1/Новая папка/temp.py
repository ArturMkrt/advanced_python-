def mergeSort(arr,order='ascending'):
    if order=='ascending':
        od = lambda x,y:x < y
    if order == 'descending':
        od = lambda x,y:x > y
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if od(L[i],R[j]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
print(mergeSort([1,2,3,4,25,122,982],'descending'))