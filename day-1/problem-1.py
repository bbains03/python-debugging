def calculate_earnings(hours, hourly_rate):
    earnings = hours * hourly_rate
    return earnings

hours_worked = "40"
pay_rate = 25

total = calculate_earnings(hours_worked, pay_rate)

print(f"Weekly earnings: ${total}")