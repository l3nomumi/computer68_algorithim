from typing import List, Optional
from models import Student
from database import Database


class StudentRepository:
    def __init__(self, db: Database):
        self.db = db

    def insert(self, student: Student) -> int:
        with self.db.get_connection() as conn:
            cur = conn.execute("""
                INSERT INTO students
                (student_id, first_name, last_name, major, faculty,
                 nickname, phonenumber, email)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                student.student_id,
                student.first_name,
                student.last_name,
                student.major,
                student.faculty,
                student.nickname,
                student.phonenumber,
                student.email
            ))
            conn.commit()
            return cur.rowcount

    def get_all(self) -> List[Student]:
        with self.db.get_connection() as conn:
            rows = conn.execute("""
                SELECT * FROM students
                ORDER BY student_id
            """).fetchall()

            return [
                Student(
                    row["student_id"],
                    row["first_name"],
                    row["last_name"],
                    row["major"],
                    row["faculty"],
                    row["nickname"],
                    row["phonenumber"],
                    row["email"]
                )
                for row in rows
            ]

    def get_by_id(self, student_id: str) -> Optional[Student]:
        with self.db.get_connection() as conn:
            row = conn.execute(
                "SELECT * FROM students WHERE student_id=?",
                (student_id,)
            ).fetchone()

            if not row:
                return None

            return Student(
                row["student_id"],
                row["first_name"],
                row["last_name"],
                row["major"],
                row["faculty"],
                row["nickname"],
                row["phonenumber"],
                row["email"]
            )

    def update(self, student: Student) -> int:
        with self.db.get_connection() as conn:
            cur = conn.execute("""
                UPDATE students
                SET first_name=?, last_name=?, major=?, faculty=?,
                    nickname=?, phonenumber=?, email=?
                WHERE student_id=?
            """, (
                student.first_name,
                student.last_name,
                student.major,
                student.faculty,
                student.nickname,
                student.phonenumber,
                student.email,
                student.student_id
            ))
            conn.commit()
            return cur.rowcount

    def delete(self, student_id: str) -> int:
        with self.db.get_connection() as conn:
            cur = conn.execute(
                "DELETE FROM students WHERE student_id=?",
                (student_id,)
            )
            conn.commit()
            return cur.rowcount

    # 🔥 เพิ่ม search
    def search(self, keyword: str) -> List[Student]:
        with self.db.get_connection() as conn:
            rows = conn.execute("""
                SELECT * FROM students
                WHERE student_id LIKE ?
                OR first_name LIKE ?
                OR last_name LIKE ?
                OR major LIKE ?
                OR faculty LIKE ?
                ORDER BY student_id
            """, tuple([f"%{keyword}%"] * 5)).fetchall()

            return [
                Student(
                    row["student_id"],
                    row["first_name"],
                    row["last_name"],
                    row["major"],
                    row["faculty"],
                    row["nickname"],
                    row["phonenumber"],
                    row["email"]
                )
                for row in rows
            ]