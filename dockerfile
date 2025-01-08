# Use the official Python image as a base
FROM python:3.9-slim

# Sets the working directory inside the container
WORKDIR /app

# Copies the current directory's contents into the container
COPY . .

# Installs Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Defines the command to run the application
CMD ["python", "health.py", "/app/sample.yaml"]
