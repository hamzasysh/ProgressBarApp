# Use an official Python runtime as a parent image
FROM python:3.13.0rc1-slim

# Install build essentials and other necessary tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libc-dev \
    libffi-dev \
    libssl-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Expose port
EXPOSE 8000

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
