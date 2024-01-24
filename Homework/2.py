class Student:
    def __init__(self, name, class_name, final_grade):
        self.name = name
        self.class_name = class_name
        self.final_grade = final_grade
        self.next_student = None

class University:
    def __init__(self):
        self.head = None

    def add_student_at_beginning(self, name, class_name, final_grade):
        new_student = Student(name, class_name, final_grade)
        new_student.next_student = self.head
        self.head = new_student

    def count_students_with_high_grades(self, threshold):
        count = 0
        current_student = self.head
        while current_student is not None:
            if current_student.final_grade >= threshold:
                count += 1
            current_student = current_student.next_student
        return count

# Example of using the classes and methods:
university = University()

# Thêm sinh viên vào đầu danh sách
university.add_student_at_beginning("Nguyen Van A", "A1", 9.5)
university.add_student_at_beginning("Tran Thi B", "A2", 7.8)
university.add_student_at_beginning("Le Van C", "B1", 8.2)

# Thống kê số lượng sinh viên có điểm tổng kết lớn hơn hoặc bằng 8
high_grade_count = university.count_students_with_high_grades(8)
print(f"Số lượng sinh viên có điểm tổng kết lớn hơn hoặc bằng 8: {high_grade_count}")