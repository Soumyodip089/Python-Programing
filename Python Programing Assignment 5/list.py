#8.Write a python program that takes any two list L and M of the same size and adds their elements together to from a new list N whose elements are sums of the corresponding elements in L and M.

L = [1, 2, 3, 4, 5]
M = [6, 7, 8, 9, 10]

N = [L[i] + M[i] for i in range(len(L))]

print("New list N:", N)