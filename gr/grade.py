def score_to_grade(score):
    if score >= 80:
        return "A", 4.0
    elif score >= 75:
        return "B+", 3.5
    elif score >= 70:
        return "B", 3.0
    elif score >= 65:
        return "C+", 2.5
    elif score >= 60:
        return "C", 2.0
    elif score >= 55:
        return "D+", 1.5
    elif score >= 50:
        return "D", 1.0
    else:
        return "F", 0.0

num_subjects = 10   # รับคะแนน 10 วิชา

total_grade_point = 0

print("\n=== ผลการเรียนแต่ละวิชา ===")
for i in range(1, num_subjects + 1):
    score = float(input(f"กรอกคะแนนวิชา {i}: "))
    grade, gp = score_to_grade(score)

    print(f"วิชา {i}: คะแนน = {score}, เกรด = {grade}")

    total_grade_point += gp

gpa = total_grade_point / num_subjects

print(f"\nGPA ของคุณคือ: {gpa:.2f}")