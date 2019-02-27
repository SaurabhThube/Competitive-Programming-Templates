def bfs(arr,s):
    queue=[]
    queue.append(s)
    visited[s]=1
    while len(queue)!=0:
        val=queue.pop()
        for i in arr[val]:
            if visited[i]==0:
                visited[i]=1
                level[i]=level[val]+1
                queue.append(i)
    return

num=input()
arr=[[]for i in xrange(num)]
for i in xrange(num-1):
    a=map(int,raw_input().split())
    arr[a[0]-1].append(a[1]-1)
    arr[a[1]-1].append(a[0]-1)
x=input()
visited=[0 for i in xrange(num)]
level=[0 for i in xrange(num)]
bfs(arr,0)
count=0
for i in level:
    if i+1==x:
        count+=1
print count
