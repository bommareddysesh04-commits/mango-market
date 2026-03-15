#!/bin/bash

# Mango Market Platform - Production Startup Script

echo "🥭 Starting Mango Market Platform in Production Mode"
echo "=================================================="

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "❌ Error: .env file not found. Please copy .env.example to .env and configure it."
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install/update dependencies
echo "📥 Installing dependencies..."
pip install -r backend/requirements.txt

# Create instance directory if it doesn't exist
mkdir -p instance/uploads/trade_licenses

# Run database migrations if needed
echo "🗄️  Checking database..."
python3 -c "
import os
import sys
sys.path.insert(0, 'backend')
from main import create_app
app = create_app()
with app.app_context():
    from main import db
    db.create_all()
    print('✅ Database ready')
"

# Start with Gunicorn
echo "🚀 Starting Gunicorn server..."
echo "   Config: backend/gunicorn_config.py"
echo "   Press Ctrl+C to stop"
echo ""

gunicorn --config backend/gunicorn_config.py backend.wsgi:app