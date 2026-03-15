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
<<<<<<< HEAD
    SECRET_KEY = os.environ.get("SECRET_KEY", "mango_market_secure_key_2026")

    # Base directory of backend
    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    # -------------------------------------------------
    # DATABASE CONFIGURATION
    # -------------------------------------------------

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

    # -------------------------------------------------
    # DATABASE ENGINE OPTIONS
    # -------------------------------------------------
=======
    # --------------------------------------------------

    SECRET_KEY = os.environ.get("SECRET_KEY", "mango_market_secure_key_2026")

    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    # --------------------------------------------------
    # DATABASE CONFIGURATION
    # --------------------------------------------------

    DATABASE_URL = os.environ.get("DATABASE_URL")

    if DATABASE_URL:
        # Production (PostgreSQL on Render)
        SQLALCHEMY_DATABASE_URI = DATABASE_URL
    else:
        # SQLite fallback for development / container
        DB_DIR = "/app/instance"
        os.makedirs(DB_DIR, exist_ok=True)

        DB_PATH = os.path.join(DB_DIR, "database.db")
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_PATH}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --------------------------------------------------
    # DATABASE ENGINE OPTIONS
    # --------------------------------------------------
>>>>>>> 743e8ae (Fix SQLite database path for Render)

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

<<<<<<< HEAD
    # -------------------------------------------------
    # EMAIL CONFIGURATION
    # -------------------------------------------------
=======
    # --------------------------------------------------
    # EMAIL CONFIGURATION
    # --------------------------------------------------
>>>>>>> 743e8ae (Fix SQLite database path for Render)

    EMAIL_USER = os.environ.get("EMAIL_USER")
    EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

<<<<<<< HEAD
    # -------------------------------------------------
    # ENCRYPTION
    # -------------------------------------------------

    FERNET_KEY = os.environ.get("FERNET_KEY")

    # -------------------------------------------------
    # SESSION SECURITY
    # -------------------------------------------------
=======
    # --------------------------------------------------
    # ENCRYPTION KEY
    # --------------------------------------------------

    FERNET_KEY = os.environ.get("FERNET_KEY")

    # --------------------------------------------------
    # SESSION SECURITY
    # --------------------------------------------------
>>>>>>> 743e8ae (Fix SQLite database path for Render)

    SESSION_COOKIE_SECURE = os.environ.get("FLASK_ENV") == "production"
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_NAME = "mango_session"
    PERMANENT_SESSION_LIFETIME = 3600
    SESSION_COOKIE_DOMAIN = None
<<<<<<< HEAD

    # -------------------------------------------------
    # TESTING
    # -------------------------------------------------

    TESTING = False
=======

    # --------------------------------------------------
    # TESTING
    # --------------------------------------------------

    TESTING = False
>>>>>>> 743e8ae (Fix SQLite database path for Render)
