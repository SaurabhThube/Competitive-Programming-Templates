def seg(node,start,end):
    if start==end:
        tree[node]=arr[start]
    else:
        mid=(start+end)/2
        seg(node*2+1,start,mid)
        seg(node*2+2,mid+1,end)
        tree[node]=min(tree[node*2+1],tree[node*2+2])
    return

def update(node,idx,start,end,val):
    if start==end:
        arr[idx]=val
        tree[node]=val
    else:
        mid=(start+end)/2
        if start<=idx and idx<=mid:
            update(2*node+1,idx,start,mid,val)
        else:
            update(2*node+2,idx,mid+1,end,val)
        tree[node]=min(tree[2*node+1],tree[2*node+2])
    return

def query(node,start,end,l,r):
    #print node,start,end,l,r
    if start>r or end<l:
        return 10**9
    if l<=start and end<=r:
        return tree[node]
    mid=(start+end)/2
    return min(query(2*node+1,start,mid,l,r),query(2*node+2,mid+1,end,l,r))



n,m=map(int,raw_input().split())
arr=map(int,raw_input().split())
num=2*n-1
tree=[1e9 for i in xrange(num+1)]
seg(0,0,n-1)
for _ in xrange(m):
    q=raw_input().split()
    if q[0]=='q':
        print query(0,0,n-1,int(q[1])-1,int(q[2])-1)
    else:
        update(0,int(q[1])-1,0,n-1,int(q[2]))


