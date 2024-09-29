class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def fractional_knapsack(W, items):
    # Sorting items based on value/weight ratio in descending order
    items.sort(key=lambda x: x.value / x.weight, reverse=True)

    total_value = 0.0
    current_weight = 0

    for item in items:
        if current_weight + item.weight <= W:
            current_weight += item.weight
            total_value += item.value
        else:
            remaining_weight = W - current_weight
            total_value += (item.value / item.weight) * remaining_weight
            break

    return total_value

if __name__ == "__main__":
    items = [
        Item(60, 10),
        Item(100, 20),
        Item(120, 30)
    ]

    W = 50
    max_value = fractional_knapsack(W, items)
    print(f"Maximum value: {max_value}")
