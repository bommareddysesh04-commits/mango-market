"""
Mango Market Platform - Configuration
Environment-based configuration for Flask application
"""

import os
from typing import Any, Dict
from sqlalchemy.pool import StaticPool


class Config:
    """Flask application configuration with environment variable support"""

    # Flask Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mango_market_secure_key_2026'
    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    # Database Configuration - Support both SQLite (dev) and PostgreSQL (prod)
    DATABASE_URL = os.environ.get('DATABASE_URL') or f'sqlite:///{os.path.join(BASE_DIR, "../instance/database.db")}'
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Database Engine Options - Different for SQLite vs PostgreSQL
    if DATABASE_URL.startswith('sqlite'):
        # SQLite configuration
        SQLALCHEMY_ENGINE_OPTIONS: Dict[str, Any] = {
            'connect_args': {
                'timeout': 30,
                'check_same_thread': False,
            },
            'poolclass': StaticPool,
            'echo': False,
        }
    else:
        # PostgreSQL configuration
        SQLALCHEMY_ENGINE_OPTIONS: Dict[str, Any] = {
            'pool_pre_ping': True,
            'pool_recycle': 300,
        }

    # Email Configuration
    EMAIL_USER = os.environ.get('EMAIL_USER')
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

    # Encryption Key
    FERNET_KEY = os.environ.get('FERNET_KEY')

    # Session Configuration - Production Security
    SESSION_COOKIE_SECURE = os.environ.get('FLASK_ENV') == 'production'  # HTTPS only in production
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    SESSION_COOKIE_NAME = 'mango_session'
    PERMANENT_SESSION_LIFETIME = 3600  # 1 hour
    SESSION_COOKIE_DOMAIN = None  # Allow localhost

    # Testing Configuration
    TESTING = False