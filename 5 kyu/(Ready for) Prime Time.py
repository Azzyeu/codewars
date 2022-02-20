def prime(n):
    primes = []
    if n < 2:
        return primes
    else:
        for i in range(2, n+1):
            if isPrime(i):
                primes.append(i)
        return primes

def isPrime(n):
    prime = True
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            prime = False
            return prime
    else:
        return prime