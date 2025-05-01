# Use lightweight Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy only the necessary files
COPY server.py .
COPY inventory.ini .
COPY restart_server.yml .

# Install required packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Ansible
RUN apt-get update && apt-get install -y ansible

# Expose the Flask app port
EXPOSE 5000

# Run the Flask app
CMD ["python", "server.py"]
