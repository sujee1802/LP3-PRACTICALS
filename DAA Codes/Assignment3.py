class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.value_per_weight = value / weight

    def __lt__(self, other):
        return self.value_per_weight < other.value_per_weight


def fractional_knapsack(items, capacity):
    """Solves the fractional Knapsack problem using a greedy method.

    Args:
        items: A list of Item objects.
        capacity: The capacity of the knapsack.

    Returns:
        The maximum value that can be placed in the knapsack.
    """

    items.sort(reverse=True)

    total_value = 0
    total_weight = 0

    for item in items:
        if total_weight + item.weight <= capacity:
            total_value += item.value
            total_weight += item.weight
        else:
            remaining_capacity = capacity - total_weight
            fraction = remaining_capacity / item.weight
            total_value += fraction * item.value
            break

    return total_value


if __name__ == "__main__":
    # Create a list of Item objects.
    items = [
        Item(60, 10),
        Item(100, 20),
        Item(120, 30),
    ]

    # Set the capacity of the knapsack.
    capacity = 50

    # Solve the fractional Knapsack problem.
    max_value = fractional_knapsack(items, capacity)

    # Print the maximum value.
    print("The maximum value that can be placed in the knapsack is:", max_value)
