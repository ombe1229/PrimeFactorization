def factorization(n):
    if n in [1, 2]:
        return [n]

    l = []
    for i in range(2, n + 1):
        while n % i == 0:
            l.append(i)
            n //= i
    return l


n = int(input())
print(factorization(n))
