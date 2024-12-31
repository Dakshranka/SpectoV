# DriveWise Backend

The DriveWise backend is a Flask-based REST API that handles student registration and appointment scheduling for a driving school.

## Project Structure

```
backend/
├── app.py              # Main application entry point
├── models/            # Data models
├── routes/           # API route handlers
├── services/         # Business logic
├── utils/           # Utility functions
└── storage.py       # Data storage interface
```

## Features

- Student Registration
- Appointment Scheduling
- Instructor Management
- Data Validation

## API Endpoints

### Student Routes
- `POST /student/register` - Register a new student
- `GET /student/<student_id>` - Get student details
- `GET /student/` - List all students

### Appointment Routes
- `POST /appointment/` - Create a new appointment
- `GET /appointment/<user_id>` - Get user's appointments
- `DELETE /appointment/<appointment_id>` - Cancel an appointment

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
python app.py
```

The server will start on `http://localhost:5000`

## Dependencies

- Flask
- Flask-CORS
- Python-dateutil
- OpenAI
- Pydantic
- LangChain (and related packages)

## Development Status

### Completed
- Basic API structure
- Student registration endpoints
- CORS configuration
- Data models

### In Progress
- Email and phone validation implementation
- Appointment scheduling logic
- Student-instructor matching

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
