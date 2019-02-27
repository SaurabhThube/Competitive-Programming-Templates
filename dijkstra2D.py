def dijkstra(x,y):
    sptSet = [[x,y]]
    jj = 0
    while (len(sptSet) != a[0]*a[1]):
        #print sptSet[jj]
        aa= sptSet[jj]
        x,y=aa[0],aa[1]
        #print x,y
        for i,j in arr:
            if x+i>=0 and x+i<a[0] and y+j>=0 and y+j<a[1]:
                if dist[x][y] + weight[x+i][y+j] < dist[x+i][y+j] and Truth[x+i][y+j] == True:
                    dist[x+i][y+j] = dist[x][y] + weight[x+i][y+j]
                #income[i] = x
        Truth[x][y] = False
        mini = 10 ** 20
        ind = [0,0]
        for i in xrange(a[0]):
            for j in xrange(a[1]):
                if dist[i][j] < mini and Truth[i][j] == True:
                    mini = dist[i][j]
                    ind = [i,j]
        #print ind
        sptSet.append(ind)
        #print sptSet
        jj += 1
        if ind[0]==val[0]-1 and ind[1]==val[1]-1:
            return dist[val[0]-1][val[1]-1]
    return 10**30

arr=[[1,0],[0,1],[-1,0],[0,-1]]
for _ in xrange(input()):
    a=map(int,raw_input().split())
    Truth=[]
    dist=[]
    weight=[]
    for i in xrange(a[0]):
        Truth.append([True for j in xrange(a[1])])
        dist.append([10**20 for j in xrange(a[1])])
        weight.append(map(int,raw_input().split()))
    val=map(int,raw_input().split())
    dist[0][0]=weight[0][0]
    if dijkstra(0,0)<=val[2]:
        print 'YES'
        print val[2]-dist[val[0]-1][val[1]-1]
    else:
        print 'NO'




