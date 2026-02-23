from models import Student
from student_repository import StudentRepository


class StudentService:
    def __init__(self, repo: StudentRepository):
        self.repo = repo

    def list_students(self):
        return self.repo.get_all()

    def create_student(self, student: Student):
        if self.repo.get_by_id(student.student_id):
            raise ValueError("รหัสนักศึกษานี้มีอยู่แล้ว")
        self.repo.insert(student)

    def update_student(self, student: Student):
        affected = self.repo.update(student)
        if affected == 0:
            raise ValueError("ไม่พบรหัสนักศึกษา")

    def delete_student(self, student_id: str):
        self.repo.delete(student_id)

    def search_students(self, keyword: str):
        if not keyword:
            return self.repo.get_all()
        return self.repo.search(keyword)

    def exists(self, student_id: str):
        return self.repo.get_by_id(student_id) is not None

    def count_by_faculty(self):
        students = self.repo.get_all()
        result = {}
        for s in students:
            result[s.faculty] = result.get(s.faculty, 0) + 1
        return result

    def count_by_major(self):
        students = self.repo.get_all()
        result = {}
        for s in students:
            result[s.major] = result.get(s.major, 0) + 1
        return result