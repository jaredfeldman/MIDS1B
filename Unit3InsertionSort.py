def insertion_sort(A):
    """Perform an insertion sort on a list"""
    for k in range (1, len(A)):
        current = A[k]
        j = k
        # check if element j - 1 is greater than current
        while j > 0 and A[j - 1] > current:
            # move element j - 1 to the right
            A[j] = A[j - 1]
            j -= 1

        # reinsert current element
        A[j] = current