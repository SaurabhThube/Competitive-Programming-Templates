'''
segtree and lazy propagation implementation for addition operation on range and finding minimum in particular range
'''
from math import ceil,log

def Utree(node,start,end,l,r,val):
    if lazy[node]!=0:
        segtree[node]+=lazy[node]
        if start!=end:
            lazy[node*2+1]=lazy[node]
            lazy[node*2+2]=lazy[node]
        lazy[node]=0
    if start>end or start>r or end<l:
        return
    if start>=l and end<=r:
        segtree[node]+=val
        if start!=end:
            lazy[node*2+1]=val
            lazy[node*2+2]=val
        return
    else:
        mid=(start+end)/2
        Utree(node*2+1,start,mid,l,r,val)
        Utree(node*2+2,mid+1,end,l,r,val)
        segtree[node]=min(segtree[node*2+1],segtree[node*2+2])
        return

def Qtree(node,start,end,l,r):
    if start>end or start>r or end<l:
        return 1e9
    if lazy[node]!=0:
        segtree[node]+=lazy[node]
        if start!=end:
            lazy[node*2+1]=lazy[node]
            lazy[node*2+2]=lazy[node]
        lazy[node]=0
    if start>=l and end<=r:
        return segtree[node]
    mid=(start+end)/2
    val1=Qtree(node*2+1,start,mid,l,r)
    val2=Qtree(node*2+2,mid+1,end,l,r)
    return min(val1,val2)


def segtreeB(node,start,end):
    if start==end:
        segtree[node]=arr[start]
    else:
        mid=(start+end)/2
        segtreeB(2*node+1,start,mid)
        segtreeB(2*node+2,mid+1,end)
        segtree[node]=min(segtree[node*2+1],segtree[node*2+2])

a=input()
numb=2*a-1
lazy=[0 for i in xrange(numb)]
segtree=[1e9 for i in xrange(numb)]
arr=map(int,raw_input().split())
segtreeB(0,0,a-1)
for _ in xrange(input()):
    q=map(int,raw_input().split())
    if q[0]==1:
        Utree(0,0,a-1,q[1]-1,q[2]-1,q[3])
    else:
        print Qtree(0,0,a-1,q[1]-1,q[2]-1)
