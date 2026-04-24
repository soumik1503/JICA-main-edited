# Base Image
FROM python:3.12-slim

# Set Environment Variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# Set Working Directory
WORKDIR /app

# Install System Dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Project Code
COPY . .

# Run collectstatic (optional during build, or can be done in entrypoint)
# RUN python manage.py collectstatic --noinput

# Expose Port (internal to container network)
EXPOSE 8000

# Command to run (Waitress)
CMD ["python", "run_waitress_server.py"]
