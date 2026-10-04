import sqlite3
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    group_name TEXT NOT NULL,
    grade INTEGER NOT NULL)
""")
conn.commit()

def show_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    if len(students) == 0:
        print("Список студентов пуст")
    else:
        print("\nСписок студентов:")
        for student in students:
            print(
                f"ID: {student[0]} | "
                f"ФИО: {student[1]} | "
                f"Группа: {student[2]} | "
                f"Оценка: {student[3]}")

def add_student():
    name = input("Введите ФИО студента: ")
    group_name = input("Введите группу: ")
    grade = int(input("Введите оценку: "))
    cursor.execute(
        "INSERT INTO students (name, group_name, grade) VALUES (?, ?, ?)",
        (name, group_name, grade))
    conn.commit()
    print("Студент добавлен")

def find_by_group():
    group_name = input("Введите название группы: ")
    cursor.execute(
        "SELECT * FROM students WHERE group_name = ?",
        (group_name,))
    students = cursor.fetchall()
    if len(students) == 0:
        print("Студенты этой группы не найдены")
    else:
        for student in students:
            print(
                f"ID: {student[0]} | "
                f"ФИО: {student[1]} | "
                f"Группа: {student[2]} | "
                f"Оценка: {student[3]}")

def find_by_grade():
    grade = int(input("Введите оценку: "))
    cursor.execute(
        "SELECT * FROM students WHERE grade = ?",
        (grade,))
    students = cursor.fetchall()
    if len(students) == 0:
        print("Студенты с такой оценкой не найдены")
    else:
        for student in students:
            print(
                f"ID: {student[0]} | "
                f"ФИО: {student[1]} | "
                f"Группа: {student[2]} | "
                f"Оценка: {student[3]}")

def change_grade():
    student_id = int(input("Введите ID студента: "))
    new_grade = int(input("Введите новую оценку: "))
    cursor.execute(
        "UPDATE students SET grade = ? WHERE id = ?",
        (new_grade, student_id))
    conn.commit()
    if cursor.rowcount > 0:
        print("Оценка изменена")
    else:
        print("Студент с таким ID не найден")

def delete_student():
    student_id = int(input("Введите ID студента: "))
    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,))
    conn.commit()
    if cursor.rowcount > 0:
        print("Студент удалён")
    else:
        print("Студент с таким ID не найден")
    show_students()

def average_grade():
    cursor.execute("SELECT AVG(grade) FROM students")
    result = cursor.fetchone()
    if result[0] is None:
        print("Студентов пока нет")
    else:
        print(f"Средняя оценка: {result[0]:.2f}")

while True:
    print("\nУЧЁТ СТУДЕНТОВ")
    print("1. Показать всех студентов")
    print("2. Добавить студента")
    print("3. Найти студентов по группе")
    print("4. Найти студентов по оценке")
    print("5. Изменить оценку")
    print("6. Удалить студента")
    print("7. Средняя оценка")
    print("0. Выход")
    choice = input("Выберите пункт: ")
    if choice == "1":
        show_students()
    elif choice == "2":
        add_student()
    elif choice == "3":
        find_by_group()
    elif choice == "4":
        find_by_grade()
    elif choice == "5":
        change_grade()
    elif choice == "6":
        delete_student()
    elif choice == "7":
        average_grade()
    elif choice == "0":
        print("Программа завершена")
        break
    else:
        print("Неверный пункт меню")


conn.close()