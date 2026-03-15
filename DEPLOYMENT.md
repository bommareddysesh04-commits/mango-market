# Mango Market Platform - Production Deployment Guide

## Overview
This guide provides deployment instructions for the Mango Market Platform across different hosting providers.

## Prerequisites
- Python 3.12+
- PostgreSQL (for production) or SQLite (for development)
- Redis (optional, for session storage)
- SSL certificate (for HTTPS)

## Environment Setup

1. Copy `.env.example` to `.env` and configure:
```bash
cp .env.example .env
# Edit .env with your production values
```

2. Generate secure keys:
```bash
# Generate SECRET_KEY (32 bytes)
python -c "import secrets; print(secrets.token_hex(32))"

# Generate FERNET_KEY (32 bytes)
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

## 1. Local Production Deployment

### Using Gunicorn
```bash
# Install dependencies
pip install -r backend/requirements.txt

# Run with Gunicorn
gunicorn --bind 0.0.0.0:5000 --workers 4 backend.wsgi:app

# Or use the provided script
./start_production.sh
```

### Using Docker
```bash
# Build and run
docker build -t mango-market .
docker run -p 5000:5000 --env-file .env mango-market
```

## 2. Render Deployment

### render.yaml
```yaml
services:
  - type: web
    name: mango-market-api
    env: python
    buildCommand: pip install -r backend/requirements.txt
    startCommand: gunicorn --bind 0.0.0.0:$PORT --workers 2 backend.wsgi:app
    envVars:
      - key: DATABASE_URL
        value: YOUR_POSTGRES_URL
      - key: SECRET_KEY
        value: YOUR_SECRET_KEY
      - key: FERNET_KEY
        value: YOUR_FERNET_KEY
      - key: CORS_ORIGINS
        value: https://your-render-app.onrender.com
```

### Steps:
1. Connect your GitHub repository to Render
2. Create a new Web Service
3. Configure environment variables
4. Deploy

## 3. Railway Deployment

### railway.json
```json
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "gunicorn --bind 0.0.0.0:$PORT --workers 2 backend.wsgi:app"
  }
}
```

### Steps:
1. Connect GitHub repository
2. Add environment variables in Railway dashboard
3. Deploy automatically

## 4. AWS EC2 Deployment

### Server Setup
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and pip
sudo apt install python3 python3-pip python3-venv -y

# Install Nginx
sudo apt install nginx -y

# Install PostgreSQL
sudo apt install postgresql postgresql-contrib -y

# Configure PostgreSQL
sudo -u postgres createuser --interactive --pwprompt mango_user
sudo -u postgres createdb -O mango_user mango_market
```

### Application Deployment
```bash
# Clone repository
git clone https://github.com/yourusername/mango-market-platform.git
cd mango-market-platform

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r backend/requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with production values

# Create systemd service
sudo nano /etc/systemd/system/mango-market.service
```

### systemd Service File
```ini
[Unit]
Description=Mango Market Platform
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/mango-market-platform
Environment="PATH=/home/ubuntu/mango-market-platform/venv/bin"
ExecStart=/home/ubuntu/mango-market-platform/venv/bin/gunicorn --bind 127.0.0.1:5000 --workers 4 backend.wsgi:app
Restart=always

[Install]
WantedBy=multi-user.target
```

### Nginx Configuration
```bash
sudo cp nginx.conf /etc/nginx/sites-available/mango-market
sudo ln -s /etc/nginx/sites-available/mango-market /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

### Start Services
```bash
sudo systemctl start mango-market
sudo systemctl enable mango-market
sudo systemctl restart nginx
```

### SSL with Let's Encrypt
```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d yourdomain.com
```

## 5. DigitalOcean VPS Deployment

### Droplet Setup
1. Create Ubuntu 22.04 droplet
2. Configure firewall:
```bash
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw --force enable
```

### Application Setup
Follow the same AWS EC2 steps above.

### Monitoring
```bash
# Install monitoring tools
sudo apt install htop iotop -y

# Check logs
sudo journalctl -u mango-market -f
sudo tail -f /var/log/nginx/error.log
```

## 6. Docker Compose Deployment

### docker-compose.yml
```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "5000:5000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/mango_market
    depends_on:
      - db
    volumes:
      - ./instance:/app/instance

  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=mango_market
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres_data:/var/lib/postgresql/data

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf
    depends_on:
      - app

volumes:
  postgres_data:
```

## Final Production Checklist

### Pre-Deployment Configuration
- [ ] Copy `.env.example` to `.env` and configure all variables
- [ ] Generate strong `SECRET_KEY` (32+ characters)
- [ ] Generate `FERNET_KEY` using `python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"`
- [ ] Set up PostgreSQL database (production) or verify SQLite (development)
- [ ] Configure email SMTP settings
- [ ] Test email sending with `python backend/send_test_otp_cli.py test@example.com`

### Security Configuration
- [ ] Set `SESSION_COOKIE_SECURE=True` in production (handled automatically)
- [ ] Configure HTTPS with SSL certificates
- [ ] Set up firewall rules (allow 80, 443, 22)
- [ ] Configure CORS_ORIGINS for production domain
- [ ] Verify rate limiting is working (5/min for login, 3/min for OTP)
- [ ] Test password hashing with `werkzeug.security`

### Application Deployment
- [ ] Choose deployment method: Docker, Gunicorn+Nginx, or cloud platform
- [ ] For Docker: Build with `docker build -t mango-market .`
- [ ] For Gunicorn: Use `gunicorn --config backend/gunicorn_config.py backend.wsgi:app`
- [ ] Configure reverse proxy (Nginx) with SSL termination
- [ ] Set up health checks at `/health` endpoint
- [ ] Enable production logging to `backend/logs/app.log`

### Database & Backup
- [ ] Run database migrations on startup
- [ ] Set up automated backups with `scripts/backup_db.sh`
- [ ] Configure backup storage (local or cloud)
- [ ] Test database connection pooling
- [ ] Verify data encryption for sensitive fields

### Monitoring & Maintenance
- [ ] Set up log rotation and monitoring
- [ ] Configure error tracking (Sentry, etc.)
- [ ] Set up uptime monitoring for `/health`
- [ ] Configure automated deployments (CI/CD)
- [ ] Set up performance monitoring

### Testing
- [ ] Test all API endpoints
- [ ] Verify frontend loads correctly
- [ ] Test user registration and login
- [ ] Test OTP verification
- [ ] Test file uploads
- [ ] Test concurrent user access
- [ ] Verify error handling (400, 401, 403, 404, 500)

### Scaling Considerations
- [ ] Configure Gunicorn workers based on CPU cores
- [ ] Set up load balancer if needed
- [ ] Configure database connection pooling
- [ ] Set up Redis for sessions (optional)
- [ ] Configure CDN for static assets

### Go-Live Checklist
- [ ] All environment variables configured
- [ ] SSL certificates installed and working
- [ ] Domain DNS configured
- [ ] Backup strategy implemented
- [ ] Monitoring and alerting set up
- [ ] Rollback plan prepared
- [ ] Team notified of deployment schedule

## Security Checklist

- [ ] Change default SECRET_KEY
- [ ] Use strong FERNET_KEY
- [ ] Configure HTTPS
- [ ] Set SESSION_COOKIE_SECURE=True
- [ ] Use environment variables for all secrets
- [ ] Configure firewall
- [ ] Regular security updates
- [ ] Monitor logs
- [ ] Backup database regularly

## Performance Optimization

- Use PostgreSQL in production
- Configure Gunicorn workers based on CPU cores
- Enable gzip compression
- Set up CDN for static files
- Configure database connection pooling
- Use Redis for sessions (optional)

## Troubleshooting

### Common Issues:
1. **Port already in use**: `sudo lsof -i :5000`
2. **Permission denied**: Check file permissions
3. **Database connection failed**: Verify DATABASE_URL
4. **Static files not loading**: Check Nginx configuration

### Health Check
```bash
curl http://localhost:5000/health
```