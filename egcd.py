def egcd(a, b):
    if b == 0:
        return a, (1, 0)
    else:
        g, (s, t) = egcd(b, a % b)

        x = t
        y = s - (a / b) * t
	return g, (x, y)

#precomputation of inverses
'''
inv[1..n]

inv[1] = 1
for a = 2..n:
    inv[i] = (p - floor(p/a)) * inv[p % a] % p
'''

mod = 10**9 + 7
N = 511111
fac = [1]*N
ifc = [1]*N
for i in xrange(2, N):
    ifc[i] = -(mod / i) * ifc[mod % i] % mod

for i in xrange(2, N):
    fac[i] = fac[i-1] * i % mod
    ifc[i] = ifc[i-1] * ifc[i] % mod

