def get_grade_result_students(name: str, marks: int, student_class: str) -> str:
    if marks >= 90:
        grade = 'A'
    elif marks >= 80:
        grade = 'B'
    elif marks >= 70:
        grade = 'C'
    elif marks >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    return f"Student: {name}, Class: {student_class}, Grade: {grade}"

# Example usage
result = get_grade_result_students("Alice", 85, "10th Grade")
print(result)

result = get_grade_result_students("Bob", 72, "9th Grade")
print(result)




#####################

def add_numbers(a: str,b: str) -> str:
    return a+b

# Example usage
result = add_numbers("Hello, ", "World!")
print(result)