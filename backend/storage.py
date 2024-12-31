from typing import Dict, Optional, List
from models import Student
import uuid

class Storage:
    def __init__(self):
        self.students: Dict[str, Student] = {}
        self.emails = set()
        self.phones = set()

    def generate_id(self) -> str:
        return str(uuid.uuid4())

    def is_email_taken(self, email: str) -> bool:
        return email in self.emails

    def is_phone_taken(self, phone: str) -> bool:
        return phone in self.phones

    def save_student(self, student: Student) -> Student:
        """
        Save a student to storage
        """
        if self.is_email_taken(student.email) and not student.id:
            raise ValueError('Email already registered')
        if self.is_phone_taken(student.phone) and not student.id:
            raise ValueError('Phone already registered')

        if not student.id:
            student.id = self.generate_id()

        self.students[student.id] = student
        self.emails.add(student.email)
        self.phones.add(student.phone)
        return student

    def get_student(self, student_id: str) -> Optional[Student]:
        """
        Get a student by ID
        """
        return self.students.get(student_id)

    def get_all_students(self) -> List[Student]:
        """
        Get all students
        """
        return list(self.students.values())
