def get_grade(grade_1, grade_2, grade_3):
    score = (grade_1 + grade_2 + grade_3)/3

    if 90 <= score <= 100: 
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70: 
        return 'D'
    elif 0 <= score < 60:
        return 'F'
    else:
        return 'Score not valid'
    
print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True