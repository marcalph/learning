# Implement a function that removes all the even elements from a given list. Name it remove_even(lst).
# O(n) spacetime
def remove_even(lst):
    # Write your code here!
    return list(filter(lambda x: x%2==1, lst))
