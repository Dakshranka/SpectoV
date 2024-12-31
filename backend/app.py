from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from datetime import datetime
import os
import openai
from models import Student
from storage import Storage
from routes.student_routes import student_bp
import speech_recognition as sr

# Initialize Flask app
app = Flask(__name__)

# Set the working directory to the backend folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Enable CORS for all routes with proper configuration
CORS(app,
     resources={r"/*": {
         "origins": ["http://localhost:3000", "http://127.0.0.1:3000"],
         "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
         "allow_headers": ["Content-Type", "Authorization"],
         "supports_credentials": True
     }})

# Initialize SocketIO for real-time communication
socketio = SocketIO(app, cors_allowed_origins=["http://localhost:3000", "http://127.0.0.1:3000"])

# Initialize Storage instance
storage = Storage()

# Chatbot session storage
sessions = {}

# Fetch OpenAI API key from environment variables for security
openai.api_key = os.getenv("OPENAI_API_KEY")

# Register blueprints
app.register_blueprint(student_bp, url_prefix='/student')

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to backend!'}), 200

# Catch-all route for 404 error handling
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"message": "Page not found"}), 404

# SocketIO event for handling incoming chatbot messages
@socketio.on('message')
def handle_message(message, user_id):
    if user_id not in sessions:
        sessions[user_id] = {'step': 0}

    step = sessions[user_id]['step']

    # Process the user message and determine the next step
    if step == 0:
        sessions[user_id]['step'] = 1
        emit('message', "Hi there! What's your full name?")
    elif step == 1:
        sessions[user_id]['step'] = 2
        emit('message', "Great! What's your email address?")
    elif step == 2:
        sessions[user_id]['step'] = 3
        emit('message', "Can you provide your phone number?")
    elif step == 3:
        sessions[user_id]['step'] = 4
        emit('message', "What's your date of birth?")
    elif step == 4:
        sessions[user_id]['step'] = 5
        emit('message', "Please provide your address.")
    elif step == 5:
        sessions[user_id]['step'] = 6
        emit('message', "Do you have a driving license? (Yes/No)")
    elif step == 6:
        sessions[user_id]['step'] = 7
        emit('message', "If you have a license, please provide the license number.")
    elif step == 7:
        sessions[user_id]['step'] = 8
        emit('message', "What transmission do you prefer? (Automatic/Manual)")
    elif step == 8:
        sessions[user_id]['step'] = 9
        emit('message', "Thanks for the info! You're now registered.")
        # Save the student information in the database
        save_student_info(user_id)
    else:
        emit('message', "Please start again by typing 'start'.")

# Function to save student info to the storage
def save_student_info(user_id):
    student_data = sessions.get(user_id)
    if student_data:
        student = Student(
            first_name=student_data.get('first_name', ''),
            last_name=student_data.get('last_name', ''),
            email=student_data.get('email', ''),
            phone=student_data.get('phone', ''),
            date_of_birth=student_data.get('date_of_birth', ''),
            address=student_data.get('address', ''),
            has_license=student_data.get('has_license', False),
            license_number=student_data.get('license_number', ''),
            preferred_transmission=student_data.get('preferred_transmission', 'automatic')
        )

        try:
            stored_student = storage.save_student(student)  # Save the student to the storage
            emit('message', f"Registration successful for {stored_student.first_name}!")
        except ValueError as e:
            emit('message', str(e))

        # Clear session after saving
        sessions.pop(user_id)

# Handle new student registration data
@socketio.on('student_data')
def handle_student_data(data, user_id):
    if user_id in sessions:
        sessions[user_id].update(data)
        emit('message', f"Received your data: {data}")

# SocketIO event for interacting with OpenAI chatbot for extra assistance (optional)
@socketio.on('chat_with_bot')
def handle_chat_with_bot(user_message, user_id):
    # Ensure session exists
    if user_id not in sessions:
        sessions[user_id] = {'step': 0}

    # Process with OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a driving school registration assistant."},
                  {"role": "user", "content": user_message}]
    )

    bot_message = response['choices'][0]['message']['content']
    emit('message', bot_message)

# SocketIO event for handling voice input
@socketio.on('voice_message')
def handle_voice_message(audio_data, user_id):
    """
    Handle incoming voice messages.
    :param audio_data: The audio file data sent by the frontend.
    :param user_id: Identifier for the user session.
    """
    recognizer = sr.Recognizer()

    try:
        # Save the audio data to a temporary file
        audio_file_path = f"temp_audio_{user_id}.wav"
        with open(audio_file_path, "wb") as f:
            f.write(audio_data)

        # Load the audio file and recognize speech
        with sr.AudioFile(audio_file_path) as source:
            audio = recognizer.record(source)
            recognized_text = recognizer.recognize_google(audio)

        # Pass recognized text to chatbot
        handle_message(recognized_text, user_id)
    except sr.UnknownValueError:
        emit('message', "Sorry, I couldn't understand the audio. Please try again.")
    except sr.RequestError as e:
        emit('message', f"Speech Recognition service error: {e}")
    except Exception as e:
        emit('message', f"An error occurred: {e}")
    finally:
        # Clean up temporary audio file
        if os.path.exists(audio_file_path):
            os.remove(audio_file_path)

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    socketio.run(app, debug=True)
