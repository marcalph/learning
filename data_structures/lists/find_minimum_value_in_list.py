# Implement a function findMinimum(lst) which finds the smallest number in the given list.
# O(1) space O(n) time

def find_minimum(arr):
    # Write your code here
    min_ = arr[0]
    for it in arr:
        if min_>it:
            min_=it
    return min_

