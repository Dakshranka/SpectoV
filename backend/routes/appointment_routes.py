from flask import Blueprint, request, jsonify
from services.appointment_service import AppointmentService

appointment_bp = Blueprint('appointment', __name__)
appointment_service = AppointmentService()

@appointment_bp.route('/', methods=['POST'])
def book_appointment():
    data = request.json
    try:
        result = appointment_service.create_appointment(data)
        return jsonify(result), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@appointment_bp.route('/<user_id>', methods=['GET'])
def get_appointments(user_id):
    appointments = appointment_service.get_user_appointments(user_id)
    return jsonify(appointments), 200

@appointment_bp.route('/<appointment_id>', methods=['DELETE'])
def cancel_appointment(appointment_id):
    try:
        result = appointment_service.cancel_appointment(appointment_id)
        return jsonify(result), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
