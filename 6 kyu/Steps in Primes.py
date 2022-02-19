def isPrime(n):
    prime = True
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            prime = False
            return prime
    else:
        return prime

def step(g, m, n):
    if n - m < g:
        return None
    for i in range(m, n+1):
        if isPrime(i) and isPrime(i+g):
            return [i,i+g]
    else:
        return None