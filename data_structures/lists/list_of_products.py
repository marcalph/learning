# Implement a function, find_product(lst), which modifies a list so that each index has a product of all the numbers present in the list except the number stored at that index.
# O(n) spacetime

def find_product(lst):
    # Write your code here.
	n = len(lst)
	products= n*[1]
	lp=1
	for i in range(n):
		products[i]=lp
		lp*=lst[i]
	rp=1
	for i in reversed(range(n)):
		products[i]*=rp
		rp*=lst[i]

	return products