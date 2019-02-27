import operator

def root(r):
    while(arr[r]!=r):
        r=arr[arr[r]]
    return r

def join(r1,r2):
    R1=root(r1)
    R2=root(r2)
    if R1==R2:
        return False
    else:
        if size[R1]>size[R2]:
            arr[R2]=arr[R1]
            size[R1]+=size[R2]
            size[R2]=0
        else:
            arr[R1]=arr[R2]
            size[R2]+=size[R1]
            size[R1]=0
        return True

def kruskal():
    cost=0
    for i in arr1:
        if join(i[0]-1,i[1]-1)==True:
            cost+=i[2]
    return cost

a=map(int,raw_input().split())
arr=[]
size=[]
for i in xrange(a[0]):
    arr.append(i)
    size.append(1)
arr1=[]
for i in xrange(a[1]):
    arr1.append(map(int,raw_input().split()))
arr1=sorted(arr1,key=operator.itemgetter(2))
print kruskal()

