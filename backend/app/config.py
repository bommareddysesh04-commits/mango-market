"""
Mango Market Platform - Configuration
Environment-based configuration for Flask application
"""

import os
from typing import Any, Dict
from sqlalchemy.pool import StaticPool


class Config:
    """Flask application configuration with environment variable support"""

    # --------------------------------------------------
    # Flask Configuration
    SECRET_KEY = os.environ.get("SECRET_KEY", "mango_market_secure_key_2026")

    # Base directory of backend
    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    # --------------------------------------------------
    # DATABASE CONFIGURATION
    # --------------------------------------------------

    # If DATABASE_URL is set (Render / PostgreSQL), use it
    DATABASE_URL = os.environ.get("DATABASE_URL")

    if DATABASE_URL:
        SQLALCHEMY_DATABASE_URI = DATABASE_URL
    else:
        # Default SQLite database for local/dev and container fallback
        DB_DIR = "/app/instance"

        # Ensure directory exists
        os.makedirs(DB_DIR, exist_ok=True)

        SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(DB_DIR, 'database.db')}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --------------------------------------------------
    # DATABASE ENGINE OPTIONS
    # --------------------------------------------------

    if SQLALCHEMY_DATABASE_URI.startswith("sqlite"):
        SQLALCHEMY_ENGINE_OPTIONS: Dict[str, Any] = {
            "connect_args": {
                "timeout": 30,
                "check_same_thread": False,
            },
            "poolclass": StaticPool,
            "echo": False,
        }
    else:
        SQLALCHEMY_ENGINE_OPTIONS: Dict[str, Any] = {
            "pool_pre_ping": True,
            "pool_recycle": 300,
        }

    # --------------------------------------------------
    # EMAIL CONFIGURATION
    # --------------------------------------------------

    EMAIL_USER = os.environ.get("EMAIL_USER")
    EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

    # --------------------------------------------------
    # ENCRYPTION KEY
    # --------------------------------------------------

    FERNET_KEY = os.environ.get("FERNET_KEY")

    # --------------------------------------------------
    # SESSION SECURITY
    # --------------------------------------------------

    SESSION_COOKIE_SECURE = os.environ.get("FLASK_ENV") == "production"
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_NAME = "mango_session"
    PERMANENT_SESSION_LIFETIME = 3600
    SESSION_COOKIE_DOMAIN = None

    # --------------------------------------------------
    # TESTING
    # --------------------------------------------------

    TESTING = False
