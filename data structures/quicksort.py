def quick_sort(list):
    length=len(list)
    if length<=1:
        return list

    else:
        pivot=list.pop()
    
    items_greater=[]
    items_lower=[]

    for item in list:
        if item>pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower)+[pivot]+quick_sort(items_greater)

print(quick_sort([2,4,7,6,5,3,9]))





 