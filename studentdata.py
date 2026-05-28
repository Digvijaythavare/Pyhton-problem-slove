student_records = {}

def add_student(name,age,grade,course):
    if name in student_records:
        print(f"Student '{name}' already exists.")

    else:
        student_records[name] = {
            'age' : age,
            'grade' : grade,
            'course' : set(course)
        }    

        print(f"Student '{name}' added successfully.")

add_student("Digvijay",21,"A+","Python")
add_student("Vijay",22,"A+","Java")

print(student_records)
