# Implement a function rearrange(lst) which rearranges the elements such that all the negative elements appear on the left and positive elements appear at the right of the list. Note that it is not necessary to maintain the sorted order of the input list.


def rearrange(lst):
    # Write your code here
    idxpos = len(lst)-1
    while lst[idxpos]>=0:
        idxpos-=1
    idxneg = 0
    while lst[idxneg]<0:
        idxneg+=1

    while idxpos>idxneg:
        if lst[idxneg]>=0 and lst[idxpos]<=0:
            lst[idxneg], lst[idxpos] = lst[idxpos], lst[idxneg]
            idxneg+=1
            idxpos-=1
            print(lst)
        else:
            idxneg+=1
    return lst


def rearrange(lst):
    leftMostPosEle = 0  # index of left most element
    # iterate the list
    for curr in range(len(lst)):
        # if negative number
        if lst[curr] < 0:
            # if not the last negative number
            if curr != leftMostPosEle:
                # swap the two
                lst[curr], lst[leftMostPosEle] = lst[leftMostPosEle], lst[curr]
            # update the last position
            leftMostPosEle += 1
    return lst
