# Start from an official image that already has Python installed
FROM python:3.12-slim

# Make /app the working folder inside the container
WORKDIR /app

# Copy the dependency list first and install it
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project into /app
COPY . .

# This is the command that runs when the container starts
CMD ["python", "app.py"]