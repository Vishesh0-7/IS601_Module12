FastAPI Calculator

This project is a FastAPI-based calculator application that performs basic arithmetic operations — addition, subtraction, multiplication, and division.
It includes logging, unit/integration/end-to-end testing, and a GitHub Actions CI workflow for automated testing.

Clone the repository
git clone https://github.com/Vishesh0-7/Calculator_FastAPI.git
cd calculator--FastApi

Create and activate a virrtual environment
python -m venv venv
source venv/bin/activate

Install dependencies
pip install -r requirements.txt
playwright install

Run the FastAPI server
uvicorn app.main:app 

Testing

The project includes three levels of testing:
Unit Tests – Verify individual calculator functions
Integration Tests – Test API endpoints
End-to-End (E2E) Tests – Simulate real user interactions using Playwright

Run all tests
pytest

Or run specific test types
pytest tests/unit
pytest tests/integration
pytest tests/e2e

Continuous Integration (CI)

This project uses GitHub Actions to automatically:

Install dependencies

Run unit and integration tests

Run Playwright end-to-end tests

