
def heapify(i,n):
    larg=i
    left=2*i+1
    right=2*i+2
    if left<n and arr[larg]<arr[left]:
        larg=left
    if right<n and arr[larg]<arr[right]:
        larg=right
    if i!=larg:
        arr[larg],arr[i]=arr[i],arr[larg]
        heapify(larg,n)


def heapSort():
    for i in xrange(n/2,-1,-1):
        heapify(i,n)

    for i in xrange(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(0,i)

n=input()
arr=map(int,raw_input().split())
heapSort()
print arr
