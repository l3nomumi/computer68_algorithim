from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QMessageBox, QHeaderView, QFileDialog
)
from PyQt6.QtGui import QIntValidator
from models import Student
import csv


class MainWindow(QMainWindow):
    def __init__(self, service):
        super().__init__()
        self.service = service

        self.setWindowTitle("Student CRUD System")
        self.resize(1100, 600)

        self._build_ui()
        self.load_data()

    # =========================
    # UI
    # =========================
    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout()
        form_layout = QHBoxLayout()
        button_layout = QHBoxLayout()
        search_layout = QHBoxLayout()

        # ===== INPUTS =====
        self.txt_student_id = QLineEdit()
        self.txt_student_id.setValidator(QIntValidator(0, 99999999))
        self.txt_student_id.setMaxLength(8)

        self.txt_first_name = QLineEdit()
        self.txt_last_name = QLineEdit()
        self.txt_major = QLineEdit()
        self.txt_faculty = QLineEdit()
        self.txt_nickname = QLineEdit()
        self.txt_phonenumber = QLineEdit()
        self.txt_email = QLineEdit()

        form_layout.addWidget(QLabel("รหัส"))
        form_layout.addWidget(self.txt_student_id)
        form_layout.addWidget(QLabel("ชื่อ"))
        form_layout.addWidget(self.txt_first_name)
        form_layout.addWidget(QLabel("นามสกุล"))
        form_layout.addWidget(self.txt_last_name)
        form_layout.addWidget(QLabel("สาขา"))
        form_layout.addWidget(self.txt_major)
        form_layout.addWidget(QLabel("คณะ"))
        form_layout.addWidget(self.txt_faculty)
        form_layout.addWidget(QLabel("ชื่อเล่น"))
        form_layout.addWidget(self.txt_nickname)
        form_layout.addWidget(QLabel("เบอร์โทร"))
        form_layout.addWidget(self.txt_phonenumber)
        form_layout.addWidget(QLabel("อีเมล"))
        form_layout.addWidget(self.txt_email)

        # ===== BUTTONS =====
        self.btn_add = QPushButton("เพิ่ม")
        self.btn_update = QPushButton("แก้ไข")
        self.btn_delete = QPushButton("ลบ")
        self.btn_report = QPushButton("รายงาน")
        self.btn_import = QPushButton("Import CSV")

        self.btn_add.clicked.connect(self.add_student)
        self.btn_update.clicked.connect(self.update_student)
        self.btn_delete.clicked.connect(self.delete_student)
        self.btn_report.clicked.connect(self.show_report)
        self.btn_import.clicked.connect(self.import_csv)

        button_layout.addWidget(self.btn_add)
        button_layout.addWidget(self.btn_update)
        button_layout.addWidget(self.btn_delete)
        button_layout.addWidget(self.btn_report)
        button_layout.addWidget(self.btn_import)

        # ===== SEARCH =====
        self.txt_search = QLineEdit()
        self.txt_search.setPlaceholderText("ค้นหา...")
        self.txt_search.returnPressed.connect(self.on_search)

        self.btn_search = QPushButton("ค้นหา")
        self.btn_search.clicked.connect(self.on_search)

        search_layout.addWidget(QLabel("Search"))
        search_layout.addWidget(self.txt_search)
        search_layout.addWidget(self.btn_search)

        # ===== TABLE =====
        self.table = QTableWidget(0, 8)
        self.table.setHorizontalHeaderLabels([
            "รหัส",
            "ชื่อ",
            "นามสกุล",
            "สาขา",
            "คณะ",
            "ชื่อเล่น",
            "เบอร์โทร",
            "อีเมล"
        ])

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setSortingEnabled(True)
        self.table.cellClicked.connect(self.fill_form_from_table)

        main_layout.addLayout(search_layout)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.table)

        central.setLayout(main_layout)

    # =========================
    # CRUD
    # =========================
    def _get_student(self):
        return Student(
            self.txt_student_id.text().strip(),
            self.txt_first_name.text().strip(),
            self.txt_last_name.text().strip(),
            self.txt_major.text().strip(),
            self.txt_faculty.text().strip(),
            self.txt_nickname.text().strip(),
            self.txt_phonenumber.text().strip(),
            self.txt_email.text().strip(),
        )

    def load_data(self):
        students = self.service.list_students()
        self._render(students)

    def _render(self, students):
        self.table.setRowCount(0)

        for row, s in enumerate(students):
            self.table.insertRow(row)

            self.table.setItem(row, 0, QTableWidgetItem(s.student_id))
            self.table.setItem(row, 1, QTableWidgetItem(s.first_name))
            self.table.setItem(row, 2, QTableWidgetItem(s.last_name))
            self.table.setItem(row, 3, QTableWidgetItem(s.major))
            self.table.setItem(row, 4, QTableWidgetItem(s.faculty))
            self.table.setItem(row, 5, QTableWidgetItem(s.nickname))
            self.table.setItem(row, 6, QTableWidgetItem(s.phonenumber))
            self.table.setItem(row, 7, QTableWidgetItem(s.email))

    def add_student(self):
        self.service.create_student(self._get_student())
        self.load_data()

    def update_student(self):
        self.service.update_student(self._get_student())
        self.load_data()

    def delete_student(self):
        student_id = self.txt_student_id.text().strip()
        self.service.delete_student(student_id)
        self.load_data()

    # =========================
    # CLICK TABLE → FILL FORM
    # =========================
    def fill_form_from_table(self, row, column):
        self.txt_student_id.setText(self.table.item(row, 0).text())
        self.txt_first_name.setText(self.table.item(row, 1).text())
        self.txt_last_name.setText(self.table.item(row, 2).text())
        self.txt_major.setText(self.table.item(row, 3).text())
        self.txt_faculty.setText(self.table.item(row, 4).text())
        self.txt_nickname.setText(self.table.item(row, 5).text())
        self.txt_phonenumber.setText(self.table.item(row, 6).text())
        self.txt_email.setText(self.table.item(row, 7).text())

    # =========================
    # SEARCH
    # =========================
    def on_search(self):
        keyword = self.txt_search.text().strip()
        students = self.service.search_students(keyword)
        self._render(students)

    # =========================
    # IMPORT CSV
    # =========================
    def import_csv(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "เลือกไฟล์ CSV", "", "CSV Files (*.csv)"
        )
        if not path:
            return

        added = 0
        updated = 0

        with open(path, newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                student = Student(
                    row["student_id"],
                    row["first_name"],
                    row["last_name"],
                    row["major"],
                    row["faculty"],
                    row["nickname"],
                    row["phonenumber"],
                    row["email"],
                )

                if self.service.exists(student.student_id):
                    self.service.update_student(student)
                    updated += 1
                else:
                    self.service.create_student(student)
                    added += 1

        self.load_data()

        QMessageBox.information(
            self,
            "Import Result",
            f"เพิ่ม: {added}\nแก้ไข: {updated}"
        )

    # =========================
    # REPORT
    # =========================
    def show_report(self):
        faculty_report = self.service.count_by_faculty()
        major_report = self.service.count_by_major()

        message = "===== รายงานตามคณะ =====\n"
        for f, c in faculty_report.items():
            message += f"{f} : {c}\n"

        message += "\n===== รายงานตามสาขา =====\n"
        for m, c in major_report.items():
            message += f"{m} : {c}\n"

        QMessageBox.information(self, "รายงานสรุป", message)