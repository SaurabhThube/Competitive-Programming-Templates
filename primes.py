def prime():
    length=4
    for i in xrange(10,10**6+1):
        j=0
        set=0
        numb=i**0.5
        while(primes[j]<=numb):
            if i%primes[j]==0:
                set=1
                break
            j+=1
        if set==0:
            primes.append(i)
            length+=1
    return length


def prime(x):
    i=2
    while(i*i<x):
        if x%i==0:
            return False
    return True


#sieve

n = 1000000
#print n
p = 2
arr = [True for i in xrange(n + 1)]
lis = []
while (p * p <= n):
    if arr[p] == True:
        lis.append(p)
        for i in xrange(2 * p, n + 1, p):
            arr[i] = False
    p += 1
