def bst(first, last, q):
    if first <= last:
        mid = first+(last-first)/2
        if counts[mid] == q:
            return True
        elif q < counts[mid]:
            return bst(first, mid - 1, q)
        else:
            return bst(mid + 1, last, q)
    else:
	upperbnd=first
	lowerbnd=last
        return False
