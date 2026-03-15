# Gunicorn configuration for Mango Market Platform

# Server socket
bind = "0.0.0.0:5000"
backlog = 2048

# Worker processes
workers = 4
worker_class = "sync"
worker_connections = 1000
threads = 2
max_requests = 1000
max_requests_jitter = 50
timeout = 120
keepalive = 2

# Logging
loglevel = "info"
accesslog = "-"
errorlog = "-"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# Process naming
proc_name = "mango-market"

# Server mechanics
preload_app = True
pidfile = "/tmp/gunicorn.pid"
user = "app"
group = "app"
tmp_upload_dir = None

# SSL (uncomment when SSL certificates are available)
# keyfile = "/path/to/ssl/private.key"
# certfile = "/path/to/ssl/certificate.crt"