# Mango Market Platform

A production-ready web application for connecting farmers, brokers, and hosts in the mango trading ecosystem.

## Features

- **Multi-role Authentication**: Separate dashboards for farmers, brokers, and hosts
- **Secure File Uploads**: Trade license document management with encryption
- **Real-time Notifications**: Email and SMS notifications for transactions
- **Payment Processing**: Integrated payment gateway for transactions
- **Weighment Management**: Digital weighment slip generation and tracking
- **Transaction History**: Complete audit trail for all marketplace activities

## Production Architecture

This application is built with production-grade features:

- **Security**: HTTPS, rate limiting, input validation, encrypted data storage
- **Scalability**: Gunicorn WSGI server, connection pooling, Docker containerization
- **Monitoring**: Comprehensive logging, health checks, error handling
- **Reliability**: Automated backups, graceful error handling, database migrations

## Project Structure

```
mango-market-platform/
├── backend/                    # Flask application
│   ├── app.py                 # Main application factory
│   ├── main.py                # Application routes and logic
│   ├── config.py              # Configuration management
│   ├── requirements.txt       # Python dependencies
│   ├── routes/                # Blueprint routes
│   ├── utils/                 # Utility functions
│   └── instance/              # Instance-specific data
├── frontend/                  # Static web files
│   ├── html/                  # HTML templates
│   ├── css/                   # Stylesheets
│   ├── js/                    # JavaScript files
│   └── assets/                # Static assets
├── scripts/                   # Utility scripts
│   ├── backup_db.sh          # Database backup script
│   ├── manage_db.py          # Database maintenance
│   └── send_test_otp_cli.py  # Email testing utility
├── logs/                      # Application logs
├── nginx.conf                 # Nginx configuration
├── Dockerfile                 # Docker container config
├── gunicorn_config.py         # Gunicorn server config
├── start_production.sh        # Production startup script
└── DEPLOYMENT.md              # Deployment guide
```

## Quick Start

### Development

1. **Clone and setup:**
   ```bash
   git clone <repository-url>
   cd mango-market-platform
   ```

2. **Install dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Run development server:**
   ```bash
   python backend/main.py
   ```

### Production

1. **Build and run with Docker:**
   ```bash
   docker build -t mango-market .
   docker run -p 8000:8000 mango-market
   ```

2. **Or use the production script:**
   ```bash
   ./start_production.sh
   ```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `FLASK_ENV` | Environment (development/production) | development |
| `SECRET_KEY` | Flask secret key | (required) |
| `DATABASE_URL` | Database connection string | sqlite:///instance/database.db |
| `SMTP_SERVER` | Email SMTP server | (required for email) |
| `SMTP_PORT` | Email SMTP port | 587 |
| `SMTP_USERNAME` | Email username | (required for email) |
| `SMTP_PASSWORD` | Email password | (required for email) |

## API Endpoints

### Authentication
- `POST /register` - User registration
- `POST /login` - User login
- `POST /logout` - User logout
- `POST /verify-otp` - OTP verification

### Farmer Endpoints
- `GET /farmer/dashboard` - Farmer dashboard
- `POST /farmer/sell-request` - Create sell request
- `GET /farmer/transactions` - Transaction history

### Broker Endpoints
- `GET /broker/dashboard` - Broker dashboard
- `POST /broker/accept-request` - Accept sell request
- `GET /broker/transactions` - Transaction history

### Host Endpoints
- `GET /host/dashboard` - Host dashboard
- `POST /host/verify-broker` - Verify broker
- `GET /host/transactions` - Transaction history

### System
- `GET /health` - Health check endpoint

## Security Features

- **Rate Limiting**: Prevents brute force attacks on authentication endpoints
- **Input Validation**: Comprehensive validation of all user inputs
- **HTTPS Only**: All production traffic served over secure connections
- **Secure Headers**: Protection against common web vulnerabilities
- **Encrypted Storage**: Sensitive data encrypted at rest
- **Audit Logging**: Complete logging of all security events

## Monitoring

### Health Checks
- Application health: `GET /health`
- Database connectivity check
- External service availability

### Logs
- Application logs: `logs/app.log`
- Server logs: `logs/gunicorn.log`
- Access logs: `logs/access.log`

## Database

### Supported Databases
- **Development**: SQLite
- **Production**: PostgreSQL

### Backup
Automated daily backups with the `scripts/backup_db.sh` script.

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for comprehensive deployment instructions.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Check the [DEPLOYMENT.md](DEPLOYMENT.md) for common issues
- Review application logs in the `logs/` directory
- Ensure all environment variables are properly configured