# -------- Builder Stage --------
FROM python:3.12-slim AS builder

# Install build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --user -r requirements.txt


# -------- Production Stage --------
FROM python:3.12-slim

# Install runtime tools
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create application user
RUN useradd --create-home --shell /bin/bash --uid 1001 app

WORKDIR /app

# Copy installed Python packages from builder
COPY --from=builder /root/.local /home/app/.local
ENV PATH=/home/app/.local/bin:$PATH

# Copy backend application
COPY backend/ ./

# Create required directories including database directory
RUN mkdir -p /app/instance \
    && mkdir -p /app/instance/uploads/trade_licenses \
    && mkdir -p /app/logs \
    && chown -R app:app /app

# Switch to non-root user
USER app

# Environment variables
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
CMD curl -f http://localhost:5000/health || exit 1

# Start Flask with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--threads", "2", "--timeout", "120", "wsgi:app"]
