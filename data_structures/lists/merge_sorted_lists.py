# Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list. Name it merge_lists(lst1, lst2).
# O(m) O(m(n+m))
def merge_lists(lst1, lst2):
    # Write your code here
    idx1, idx2 = 0, 0
    while idx1 < len(lst1) and idx2 < len(lst2):
        if lst1[idx1] >= lst2[idx2]:
            lst1.insert(idx2, lst2[idx2])
            idx2 +=1
        idx1 +=1

    if idx2 < len(lst2):  # Append whatever is left of list2 to list1
        lst1.extend(lst2[idx2:])
    return lst1

