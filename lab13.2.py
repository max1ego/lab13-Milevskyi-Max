from student import STUDENT

students = [
    STUDENT("Олександр", "Петров", 2002, [5, 4, 5, 5, 4]),
    STUDENT("Марія", "Іванова", 2003, [4, 5, 4, 5, 5]),
    STUDENT("Іван", "Ковальчук", 2001, [3, 4, 5, 3, 4]),
    STUDENT("Ольга", "Сидоренко", 2002, [5, 5, 5, 5, 5]),
    STUDENT("Андрій", "Шевченко", 2003, [4, 5, 4, 4, 4]),
    STUDENT("Світлана", "Мельник", 2001, [5, 4, 5, 5, 5]),
    STUDENT("Юрій", "Лисенко", 2003, [3, 4, 3, 3, 4]),
    STUDENT("Ірина", "Тарасенко", 2002, [5, 5, 5, 5, 4]),
    STUDENT("Дмитро", "Кравченко", 2004, [4, 4, 4, 4, 5])
]

print("Студенти, які отримують стипендію:")
for student in students:
    if student.AverMark > 4.5:
        student.DisplayAll()
        print("-" * 30)
