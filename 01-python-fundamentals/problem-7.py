def find_highest(numbers):
    highest = numbers[0]

    for number in numbers:
        if number > highest:
            highest = number

    return highest

scores = [-10, -5, -20, -3]
result = find_highest(scores)

print(f"Highest score: {result}")