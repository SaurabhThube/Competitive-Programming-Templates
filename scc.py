def dfs(x):
    visited[x]=1
    for i in arr[x]:
        if visited[i]==0:
            dfs(i)
    mains.append(x)
    return

def dfs1(x,count):
    visited1[x]=True
    count+=1
    for i in arr1[x]:
        if visited1[i]==False:
           count+= dfs1(i,0)
    return count


def scc():
    #mains=[]
    for i in xrange(a[0]):
        if visited[i]==0:
           dfs(i)
    stack=mains[:]
    odd,even=0,0
    while(len(stack)!=0):
        x=stack.pop()
        if visited1[x]==False:
            count=dfs1(x,0)
            if count%2==0:
                even+=count
            else:
                odd+=count
    return odd-even



a=map(int,raw_input().split())
arr=[]
arr1=[]
visited=[]
visited1=[]
mains=[]
for i in xrange(a[0]):
    arr.append([])
    arr1.append([])
    visited.append(0)
    visited1.append(False)
for i in xrange(a[1]):
    b=map(int,raw_input().split())
    arr[b[0]-1].append(b[1]-1)
    arr1[b[1]-1].append(b[0]-1)
print scc()
