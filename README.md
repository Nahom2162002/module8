FastAPI Calculator Application
This is a FastAPI-based web application that provides user authentication and a calculator interface for performing and storing calculations.
It includes a frontend (HTML templates + static files), a backend API, and automated tests (unit, integration, and end-to-end).

Prerequisites
Before running the application, ensure you have:

Python 3.10+ installed

pip (Python package manager)

virtualenv (recommended)

Redis running locally (for authentication token management)

Setup & Running the Application
Clone or extract the project

bash
Copy
Edit
git clone <repo_url>
cd module8
Create and activate a virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate     # On macOS/Linux
venv\Scripts\activate        # On Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Initialize the database

bash
Copy
Edit
python app/database_init.py
Run Redis
If you have Redis installed locally:

bash
Copy
Edit
redis-server
Or use Docker:

bash
Copy
Edit
docker run -d -p 6379:6379 redis
Start the FastAPI application

bash
Copy
Edit
uvicorn app.main:app --reload
Access the app

Open your browser at http://127.0.0.1:8000

API documentation available at:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

Running Tests Locally
This project contains unit, integration, and end-to-end (E2E) tests located in the tests/ directory.

Ensure dependencies are installed (including pytest and httpx):

bash
Copy
Edit
pip install -r requirements.txt
Run all tests

bash
Copy
Edit
pytest
Run tests with coverage

bash
Copy
Edit
pytest --cov=app --cov-report=term-missing
Generate an HTML coverage report

bash
Copy
Edit
pytest --cov=app --cov-report=html
open htmlcov/index.html   # macOS
start htmlcov/index.html  # Windows
Project Structure
csharp
Copy
Edit
app/
  ├── auth/          # Authentication logic (JWT, Redis)
  ├── core/          # Configurations
  ├── models/        # Database models
  ├── schemas/       # Pydantic schemas
  ├── database.py    # DB connection
  ├── main.py        # FastAPI entrypoint
  ├── user.py        # User routes
templates/           # HTML templates
static/              # Static files (CSS, JS)
tests/               # Automated tests