def isArrayInSortedOrder(A):
    if len(A)==1:
        return True
    return A[0] <= A[1] and sorted(A[:])

A= [1,2,1,3,6,4,8,4,2]
print(isArrayInSortedOrder(A))
