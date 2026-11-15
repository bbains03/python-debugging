def calculate_total(prices):
    total = 0

    for price in prices:
        total = price

    return total

items = [20, 35, 15]
result = calculate_total(items)

print(f"Cart total: ${result}")