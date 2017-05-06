#!/usr/bin/python


def binary_search(blist, item):
    '''
    blist: List to do binary search on
    item: what you're searching for
    Return: location of item
    '''
    low = 0
    high = len(blist)-1

    while low <= high:
        mid = (low + high)/2
        print "Middle: %i" % mid
        guess = blist[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

THELIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 19, 22, 33, 44, 55, 66, 77, 88, 91, 94, 102]

print binary_search(THELIST, 4)
#print binary_search(THELIST, 77)



