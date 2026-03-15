"""
WSGI Entry Point for Mango Market Platform
Used by Gunicorn in production deployment
"""

from main import create_app

# Create the Flask application instance
app = create_app()

if __name__ == "__main__":
    app.run()