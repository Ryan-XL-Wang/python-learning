def binary(list1, item):
    first = 0
    last = len(list1)-1
    while first <= last:
        mid = (last+first)//2
        if item == list1[mid]:
            return True
        else:
            if item > list1[mid]:
                first = mid
            else:
                last = mid
    return False

def select(alist):
    #this worse is n(n+1)/2 comparesion, n pass
    #每轮找最小值
    compare = 0
    lenth = len(alist)
    last = lenth - 1
    for i in range(0, lenth):
        for i2 in range(i, lenth):
            
            if alist[i] > alist[i2]:
                c+= 1
                alist[i], alist[i2] = alist[i2], alist[i]
    return alist, compare

def shell_sort(alist):
    
    #how many sublist can we get
    subs = len(alist)//2
    #when we still have sublist to sort
    while subs > 0:
        for start_pos in range(subs):
            #use a insert sort for items we get based on the number of sublists(gap)
            gap_insert_sort(alist, start_pos, subs)
        #doing more specific sublists(gaps), until we get 0 sublist to sort
        subs = subs//2

def gap_insert_sort(alist, start, gap):
    #for example, if we have am 8 item list. we get 2 sublist.
    #Then we have 4th compare to first, then the next time, 4th compare to 8th
    for i in range(start + gap, len(alist), gap):
        #save the 4th value
        current = alist[i]#if 8, start from 4
        current_pos = i
        # when the item beyond current value is larger then current, change position
        while current_pos >= gap and alist[current_pos - gap] > current:
            #the 4th value become 0th
            alist[current_pos] = alist[current_pos - gap]
            current_pos = current_pos - gap
        #if current_pos changed, 4 become 0, then 0 will take 4th value
        alist[current_pos] = current