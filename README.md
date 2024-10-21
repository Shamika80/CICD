# Simple Flask Sum API

This is a simple Flask application that provides an API endpoint to calculate the sum of two numbers.

## Features

*   API endpoint `/sum` to calculate the sum of two numbers.
*   Error handling for missing parameters.
*   Unit tests to ensure functionality.
*   CI/CD pipeline using GitHub Actions to automate building and testing.

## Getting Started

1.  Clone the repository: `git clone <repository_url>`
2.  Install dependencies: `pip install -r requirements.txt`
3.  Run the app: `python app.py`

## Usage

Send a POST request to `/sum` with a JSON payload containing `num1` and `num2`:

```json
{
    "num1": 5,
    "num2": 3
}
