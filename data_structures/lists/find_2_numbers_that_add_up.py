# In this problem, you have to implement the find_sum(lst,k) function which will take a number k as input and return two numbers that add up to k.
# O(n) spacetime
def find_sum(lst, k):
    # Write your code here
    viewed = set()
    for l in lst:
        target = k-l
        if target in viewed:
            return [target, l]
        else:
            viewed.add(l)
