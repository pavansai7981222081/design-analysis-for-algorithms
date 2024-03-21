def pack_containers(weights, volumes, container_capacity):
    n = len(weights)
    dp = [[0] * (container_capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, container_capacity + 1):
            dp[i][j] = dp[i - 1][j]
            if volumes[i - 1] <= j:
                dp[i][j] = max(dp[i][j], weights[i - 1] + dp[i - 1][j - volumes[i - 1]])

    packed_items = []
    i, j = n, container_capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            packed_items.append(i - 1)
            j -= volumes[i - 1]
        i -= 1

    return dp[n][container_capacity], packed_items

weights = [2, 3, 5, 7, 1, 4, 1]
volumes = [1, 2, 3, 4, 5, 6, 7]
container_capacity = 10
total_weight, packed_items = pack_containers(weights, volumes, container_capacity)
print(f"Total weight packed: {total_weight}")
print(f"Packed items: {packed_items}")
