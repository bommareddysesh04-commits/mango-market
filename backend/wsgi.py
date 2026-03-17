"""
WSGI Entry Point for Mango Market Platform
Used by Gunicorn in production deployment
"""

from main import create_app
import os

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)