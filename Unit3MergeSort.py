def merge_sort(A):
    """Perform a merge sort on a list, A"""
    # a list with one element is already sorted
    if len(A) < 2: return

    # otherwise, split the list in half
    A1 = A[0:len(A)//2]
    A2 = A[len(A)//2:]

    # recursively sort each half
    merge_sort(A1)
    merge_sort(A2)

    # merge A1 and A2 into A
    del A[:]
    while len(A1) + len(A2) > 0:
        if len(A2) == 0 or (len(A1) > 0 and A1[0] < A2[0]):
            A.append(A1.pop(0))
        else:
            A.append(A2.pop(0))