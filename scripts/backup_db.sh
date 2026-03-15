#!/bin/bash

# Mango Market Platform - Database Backup Script
# This script creates backups of PostgreSQL database

set -e  # Exit on any error

# Configuration
BACKUP_DIR="./backups"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_NAME="mango_market_backup_${TIMESTAMP}"

# Database configuration from environment
DB_HOST=${DB_HOST:-"localhost"}
DB_PORT=${DB_PORT:-"5432"}
DB_NAME=${DB_NAME:-"mango_market"}
DB_USER=${DB_USER}
DB_PASSWORD=${DB_PASSWORD}

# Check if required environment variables are set
if [ -z "$DB_USER" ] || [ -z "$DB_PASSWORD" ]; then
    echo "Error: DB_USER and DB_PASSWORD environment variables must be set"
    exit 1
fi

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

echo "Starting database backup: $BACKUP_NAME"
echo "Database: $DB_NAME on $DB_HOST:$DB_PORT"

# Set PGPASSWORD for pg_dump
export PGPASSWORD="$DB_PASSWORD"

# Create backup using pg_dump
pg_dump \
    --host="$DB_HOST" \
    --port="$DB_PORT" \
    --username="$DB_USER" \
    --dbname="$DB_NAME" \
    --format=custom \
    --compress=9 \
    --verbose \
    --file="$BACKUP_DIR/$BACKUP_NAME.backup"

# Unset PGPASSWORD for security
unset PGPASSWORD

echo "Backup completed successfully: $BACKUP_DIR/$BACKUP_NAME.backup"

# Create a compressed archive
echo "Creating compressed archive..."
tar -czf "$BACKUP_DIR/$BACKUP_NAME.tar.gz" -C "$BACKUP_DIR" "$BACKUP_NAME.backup"

# Remove the uncompressed backup file
rm "$BACKUP_DIR/$BACKUP_NAME.backup"

echo "Compressed backup created: $BACKUP_DIR/$BACKUP_NAME.tar.gz"

# Clean up old backups (keep last 30 days)
echo "Cleaning up old backups..."
find "$BACKUP_DIR" -name "mango_market_backup_*.tar.gz" -mtime +30 -delete

echo "Backup process completed successfully"

# Optional: Upload to cloud storage (uncomment and configure as needed)
# aws s3 cp "$BACKUP_DIR/$BACKUP_NAME.tar.gz" "s3://your-backup-bucket/$BACKUP_NAME.tar.gz"