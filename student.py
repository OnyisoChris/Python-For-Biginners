from classstudent import student

student1 = student("Barbs", "Forensics", 4.2, False)
student2 = student("Patty", "Engineering", 3.6, True)

print(student1.name)
print(student2.gpa)
print(student1.on_honor_roll())
print(student2.on_honor_roll())