from datetime import datetime
from models import Appointment, AppointmentStatus
from storage import storage

class AppointmentService:
    def create_appointment(self, data):
        # todo: implement this
        return {'message': 'Appointment created successfully'}
    
    def get_user_appointments(self, user_id):
        # todo: implement this
        return []

    def cancel_appointment(self, appointment_id):
        # todo: implement this
        return {'message': 'Appointment cancelled successfully'}
