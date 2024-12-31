from dataclasses import dataclass
from datetime import datetime

@dataclass
class Student:
    first_name: str
    last_name: str
    email: str
    phone: str
    date_of_birth: str
    address: str
    has_license: bool = False
    license_number: str = ""
    preferred_transmission: str = "automatic"
    id: str = None  # Will be set by storage

    def to_dict(self):
        return {
            'id': self.id,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'dateOfBirth': self.date_of_birth,
            'address': self.address,
            'hasLicense': self.has_license,
            'licenseNumber': self.license_number,
            'preferredTransmission': self.preferred_transmission
        }

    @staticmethod
    def from_dict(data):
        return Student(
            id=data.get('id'),
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
