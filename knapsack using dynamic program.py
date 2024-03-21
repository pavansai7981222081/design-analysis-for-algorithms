def knapsack_dynamic_programming(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find the items included in the knapsack
    selected_items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
        i -= 1

    total_profit = dp[n][capacity]
    total_weight = sum(weights[item] for item in selected_items)

    return total_profit, total_weight, selected_items[::-1]

# Input your specific data here
values = [int(x) for x in input("Enter the values (separated by spaces): ").split()]
weights = [int(x) for x in input("Enter the weights (separated by spaces): ").split()]
capacity = int(input("Enter the capacity of the knapsack: "))

max_value, total_weight, selected_items = knapsack_dynamic_programming(values, weights, capacity)

print(f"Maximum value: {max_value}")
print(f"Total weight: {total_weight}")
print(f"Selected items (indices): {selected_items}")
