def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

n = 12
print("Factors of", n, "are:", find_factors(n))
