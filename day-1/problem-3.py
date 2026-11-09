def calculate_grade(score):
    if score >= 60:
        return "D"
    elif score >= 70:
        return "C"
    elif score >= 80:
        return "B"
    elif score >= 90:
        return "A"
    else:
        return "F"

student_score = 85

grade = calculate_grade(student_score)

print(f"Student grade: {grade}")