def binomial_coefficient(n, k):
    C = [[0 for _ in range(k+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]

    return C[n][k]

n = 5
k = 2
print("Binomial coefficient of", n, "choose", k, "is", binomial_coefficient(n, k))
