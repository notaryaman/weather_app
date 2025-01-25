# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY weather.py .

# Install Python dependencies
RUN pip install requests

# Define the default command to run the script
CMD ["python", "weather.py"]
