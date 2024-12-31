from models import Student
from storage import Storage

class StudentService:
    def __init__(self):
        self.storage = Storage()

    def register_student(self, data):
        """
        Register a new student with all their information in a single step
        """
        student = Student(
            first_name=data['firstName'],
            last_name=data['lastName'],
            email=data['email'],
            phone=data['phone'],
            date_of_birth=data['dateOfBirth'],
            address=data['address'],
            has_license=data.get('hasLicense', False),
            license_number=data.get('licenseNumber', ''),
            preferred_transmission=data.get('preferredTransmission', 'automatic')
        )
        
        return self.storage.save_student(student)

    def get_student(self, student_id):
        """
        Get a student by their ID
        """
        return self.storage.get_student(student_id)

    def get_all_students(self):
        """
        Get all students
        """
        return self.storage.get_all_students()
