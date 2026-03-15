# Scripts Directory

This directory contains utility scripts for the Mango Market Platform.

## Available Scripts

### backup_db.sh
Automated PostgreSQL database backup script.

**Usage:**
```bash
# Set environment variables
export DB_HOST=localhost
export DB_PORT=5432
export DB_NAME=mango_market
export DB_USER=your_user
export DB_PASSWORD=your_password

# Run backup
./scripts/backup_db.sh
```

**Features:**
- Creates compressed PostgreSQL backups
- Automatic cleanup of old backups (30+ days)
- Configurable via environment variables

### manage_db.py
Database maintenance script for SQLite databases.

**Usage:**
```bash
python scripts/manage_db.py --db instance/database.db
```

**Features:**
- Backs up SQLite database
- Removes duplicate order_id entries
- Creates unique indexes

### send_test_otp_cli.py
Command-line utility to test email OTP sending.

**Usage:**
```bash
python scripts/send_test_otp_cli.py recipient@example.com
```

**Features:**
- Tests SMTP configuration
- Sends test OTP emails
- Returns appropriate exit codes

## Setup

Make scripts executable:
```bash
chmod +x scripts/*.sh
```

## Environment Variables

For backup_db.sh, set these environment variables:
- `DB_HOST`: Database host (default: localhost)
- `DB_PORT`: Database port (default: 5432)
- `DB_NAME`: Database name (default: mango_market)
- `DB_USER`: Database username (required)
- `DB_PASSWORD`: Database password (required)