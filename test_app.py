"""
Unit tests for the devops-demo Flask application.

Run with: python -m pytest test_app.py
"""
import unittest
from app import app


class TestApp(unittest.TestCase):
    """Tests for the devops-demo Flask application."""

    def setUp(self):
        """Create a test client for each test."""
        self.app = app.test_client()
        self.app.testing = True

    # ------------------------------------------------------------------
    # Landing page tests
    # ------------------------------------------------------------------
    def test_home_page_returns_200(self):
        """The home page should return a 200 status code."""
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_title(self):
        """The home page should contain the expected heading."""
        response = self.app.get("/")
        self.assertIn(b"DevOps", response.data)

    # ------------------------------------------------------------------
    # Greeting endpoint tests
    # ------------------------------------------------------------------
    def test_greet_endpoint_returns_200(self):
        """The /greet/<name> endpoint should return 200."""
        response = self.app.get("/greet/Alice")
        self.assertEqual(response.status_code, 200)

    def test_greet_endpoint_contains_name(self):
        """The greeting should include the provided name."""
        response = self.app.get("/greet/Bob")
        self.assertIn(b"Bob", response.data)

    # ------------------------------------------------------------------
    # Health endpoint tests
    # ------------------------------------------------------------------
    def test_health_endpoint_returns_200(self):
        """The /health endpoint should return 200."""
        response = self.app.get("/health")
        self.assertEqual(response.status_code, 200)

    def test_health_endpoint_returns_json(self):
        """The /health endpoint should return JSON with a healthy status."""
        response = self.app.get("/health")
        data = response.get_json()
        self.assertEqual(data["status"], "healthy")

    # ------------------------------------------------------------------
    # Addition endpoint tests
    # ------------------------------------------------------------------
    def test_add_endpoint_two_plus_two(self):
        """The /api/add/<a>/<b> endpoint should correctly add 2 + 2."""
        response = self.app.get("/api/add/2/2")
        data = response.get_json()
        self.assertEqual(data["result"], 4)

    def test_add_endpoint_zero_plus_zero(self):
        """The /api/add/<a>/<b> endpoint should correctly add 0 + 0."""
        response = self.app.get("/api/add/0/0")
        data = response.get_json()
        self.assertEqual(data["result"], 0)

    # ------------------------------------------------------------------
    # Input sanitization tests
    # ------------------------------------------------------------------
    def test_clean_input_removes_html_tags(self):
        """clean_input should strip out HTML tags from the input."""
        from app import clean_input
        result = clean_input("<script>alert('xss')</script>")
        self.assertNotIn("<", result)
        self.assertNotIn(">", result)

    def test_clean_input_keeps_safe_text(self):
        """clean_input should keep plain alphanumeric text."""
        from app import clean_input
        result = clean_input("Alice")
        self.assertEqual(result, "Alice")


if __name__ == "__main__":
    unittest.main()