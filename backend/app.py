"""
Mango Market Platform - Entry Point
Imports create_app from consolidated main.py
Handles all three systems: Farmer, Broker, and Host
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import create_app

# Create the Flask app for Gunicorn
app = create_app()


if __name__ == '__main__':
    print("\n🥭 Starting Mango Market Platform...")
    print("   Creating Flask app with all systems (Farmer, Broker, Host)...\n")

    # Production-ready configuration
    print("\n🚀 Starting server on http://0.0.0.0:5000")
    print("   Press CTRL+C to stop\n")

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
