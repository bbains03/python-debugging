def calculate_total(price, tax_rate):
    total = price + (price * tax_rate)
    return total

product_price = 100
tax_rate = "0.12"

final_price = calculate_total(product_price, tax_rate)

print(f"Total price: ${final_price}")