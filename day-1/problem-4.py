def calculate_inventory(items):
    total = 0

    for i in range(len(items) - 1):
        total += items[i]

    return total


inventory = [12, 8, 15, 6, 9]

result = calculate_inventory(inventory)

print(f"Total inventory: {result}")