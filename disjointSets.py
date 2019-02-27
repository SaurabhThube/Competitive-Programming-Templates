def root(x):
    while(arr[x]!=x):
        x=arr[arr[x]]
    return x
def join(x,y):
    r1=root(x)
    r2=root(y)
    if r1==r2:
        return
    if size[r1]>size[r2]:
        size[r1]+=size[r2]
        size[r2]=0
        arr[r2]=arr[r1] #assigning root of r1 as root of r2
    else:
        size[r2]+=size[r1]
        size[r1]=0
        arr[r1]=arr[r2]
    return

a=map(int,raw_input().split())
arr=[]
size=[]
for i in xrange(a[0]):
    arr.append(i)
    size.append(1)
for _ in xrange(a[1]):
    q=map(int,raw_input().split())
    join(q[0]-1,q[1]-1)
