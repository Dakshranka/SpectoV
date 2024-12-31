from flask import Blueprint, request, jsonify
from services.student_service import StudentService
from utils.validators import validate_email, validate_phone
from datetime import datetime

student_bp = Blueprint('student', __name__)
student_service = StudentService()

@student_bp.route('/register', methods=['POST'])
def register_student():
    data = request.json
    
    # Validate required fields
    required_fields = ['firstName', 'lastName', 'email', 'phone', 'dateOfBirth', 'address']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    # Validate email and phone
    if not validate_email(data['email']):
        return jsonify({'error': 'Invalid email format'}), 400
    if not validate_phone(data['phone']):
        return jsonify({'error': 'Invalid phone format'}), 400

    try:
        result = student_service.register_student(data)
        return jsonify(result), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@student_bp.route('/', methods=['GET'])
def list_students():
    students = student_service.get_all_students()
    return jsonify(students), 200

@student_bp.route('/<student_id>', methods=['GET'])
def get_student(student_id):
    student = student_service.get_student(student_id)
    if not student:
        return jsonify({'error': 'Student not found'}), 404
    return jsonify(student), 200
