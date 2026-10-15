# devops-demo KULDEEP - 123B1B118

This is a simple Python web application used for demonstrating **Jenkins Pipeline integration with GitHub**.

## Project Structure

- `index.html` - A simple landing page.
- `app.py` - The main Python application.
- `test_app.py` - Unit tests for the application.
- `Jenkinsfile` - Jenkins Declarative Pipeline configuration.

## Purpose

This demo shows a CI/CD pipeline that:
1. **Checkout** - Retrieves the source code from a GitHub repository.
2. **Build** - Verifies the Python installation.
3. **Test** - Runs unit tests and fails the pipeline if any test fails.
4. **Result** - Prints a clear success/failure message.

## Getting Started

```bash
pip install -r requirements.txt
python app.py
```

Then open your browser and go to `http://localhost:5000`.

## License

MIT License.
