import time

def sieve(n):
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3, int(n**0.5+1), 2):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index+i
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime

start = time.time()
primes = sieve(1000000)
length = 0
Max = 0
l = len(primes)
for i in range(len(primes)):
    for j in range(i+length,l):
        sol = sum(primes[i:j])
        if sol < 1000000:
            if sol in primes:
                length = j-i
                Max = sol
        else:
            l = j+1
            break
end = time.time()

print(f" answer: {Max}")
print(f" execution time: {end - start}")