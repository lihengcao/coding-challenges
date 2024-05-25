up_to = int(2e6)  # 2 million

table = [True for _ in range(up_to + 1)]

primes = []

i = 2
while i < len(table):  # Sieve of Eratosthenes
    if table[i]:
        primes.append(i)
        for j in range(i, len(table), i):
            table[j] = False
    i += 1

print(sum(primes))
