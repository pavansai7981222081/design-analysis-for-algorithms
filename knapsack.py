def knapsack_greedy(values, weights, capacity):
   
    ratios = [(v / w) for v, w in zip(values, weights)]

    
    sorted_items = sorted(zip(ratios, values, weights), reverse=True)

    total_value = 0
    total_weight = 0
    selected_items = []

    for ratio, value, weight in sorted_items:
        if total_weight + weight <= capacity:
            total_value += value
            total_weight += weight
            selected_items.append((value, weight))

    return total_value, selected_items


values = [2,2,3,4]
weights = [2,2,1,1]
capacity = 2

max_value, selected_items = knapsack_greedy(values, weights, capacity)

print("Maximum value:", max_value)
print("Selected items:", selected_items)
