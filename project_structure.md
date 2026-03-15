# Mango Market Platform - Complete File Structure

This document contains the complete file and folder structure of the mango-market-platform project as of March 15, 2026 (updated after file deletions).

## Root Directory Files
- .env
- requirements.txt

## Directory Tree

```
mango-market-platform/
├── .env
├── requirements.txt
├── .venv/
│   └── (Python virtual environment - detailed structure below)
├── backend/
│   ├── .env
│   ├── app.py
│   ├── audit_utils.py
│   ├── database.db
│   ├── email_service.py
│   ├── encryption_utils.py
│   ├── main.py
│   ├── manage_db.py
│   ├── notification_utils.py
│   ├── send_test_otp_cli.py
│   ├── server.py
│   ├── SMTP_README.md
│   ├── __pycache__/
│   │   ├── audit_utils.cpython-312.pyc
│   │   ├── audit_utils.cpython-313.pyc
│   │   ├── email_service.cpython-312.pyc
│   │   ├── email_service.cpython-313.pyc
│   │   ├── encryption_utils.cpython-312.pyc
│   │   ├── encryption_utils.cpython-313.pyc
│   │   ├── main.cpython-312.pyc
│   │   ├── main.cpython-313.pyc
│   │   ├── notification_utils.cpython-312.pyc
│   │   └── notification_utils.cpython-313.pyc
│   ├── instance/
│   │   └── uploads/
│   │       └── trade_licenses/
│   │           └── broker_4_20260308_064521_payment_receipt_2.pdf
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── host_routes.py
│   │   └── __pycache__/
│   │       ├── __init__.cpython-312.pyc
│   │       ├── __init__.cpython-313.pyc
│   │       ├── host_routes.cpython-312.pyc
│   │       └── host_routes.cpython-313.pyc
│   └── utils/
├── frontend/
│   ├── assets/
│   │   └── images/
│   ├── css/
│   │   ├── accepted.css
│   │   ├── admin_verify_brokers.css
│   │   ├── auth-modern.css
│   │   ├── auth.css
│   │   ├── broker.css
│   │   ├── broker_dashboard.css
│   │   ├── broker_login.css
│   │   ├── broker_profile.css
│   │   ├── components.css
│   │   ├── farmer.css
│   │   ├── farmer_dashboard.css
│   │   ├── farmer_login.css
│   │   ├── farmer_profile.css
│   │   ├── home.css
│   │   ├── host_access.css
│   │   ├── host_dashboard.css
│   │   ├── new_broker_register.css
│   │   ├── new_farmer_register.css
│   │   ├── payments.css
│   │   ├── sell_request.css
│   │   ├── transactions.css
│   │   └── weighment.css
│   ├── html/
│   │   ├── accepted.html
│   │   ├── broker_dashboard.html
│   │   ├── broker_login.html
│   │   ├── broker_profile.html
│   │   ├── farmer_dashboard.html
│   │   ├── farmer_login.html
│   │   ├── farmer_profile.html
│   │   ├── home.html
│   │   ├── host_access.html
│   │   ├── host_dashboard.html
│   │   ├── new_broker_register.html
│   │   ├── new_farmer_register.html
│   │   ├── payments.html
│   │   ├── sell_request.html
│   │   ├── transactions.html
│   │   └── weighment.html
│   └── js/
│       ├── accepted.js
│       ├── api.js
│       ├── auth.js
│       ├── broker.js
│       ├── broker_profile.js
│       ├── farmer.js
│       ├── farmer_profile.js
│       ├── host_access.js
│       ├── host_dashboard.js
│       ├── host_verify.js
│       ├── new_broker_register.js
│       ├── payment_processor.js
│       └── transactions.js
├── instance/
│   ├── database.db
│   └── fernet.key
└── project_structure.md (this file)
```

## Detailed .venv Structure (Virtual Environment)
The .venv folder contains the Python virtual environment with installed packages. Below is a summary of the key components:

- **Lib/site-packages/**: Contains installed Python packages including:
  - fastapi, uvicorn, werkzeug, pytest, sqlalchemy, starlette, and other dependencies
  - Compiled Python bytecode files (.pyc)
  - Package metadata and licenses

- **Scripts/**: Contains executable scripts for the virtual environment:
  - activate, activate.bat, Activate.ps1 (activation scripts)
  - python.exe, pip.exe, pytest.exe, uvicorn.exe, etc. (Python executables)

Note: The .venv folder is typically excluded from version control and recreated during setup.

## Changes Made
- Removed multiple guide and test files from root directory (INTEGRATION_TEST_GUIDE.md, QUICK_RESPONSIVE_TEST.md, QUICKSTART.md, README_INTEGRATION.md, RESPONSIVE_DESIGN_GUIDE.md, RESPONSIVE_VERIFICATION_GUIDE.md, START_HERE.md, STARTUP_GUIDE.py, test_download.py, verify_setup.py)
- Removed database backup files from instance/ directory
- Kept core project files and virtual environment structure intact