def calculate_earnings(hours , hourly_rate):
    earnings = hours * hourly_rate
    return earnings

hours = 40
hourly_rate = 25

total = calculate_earnings(hours, hourly_rate)

print(f"Weekly earnings: ${total}")