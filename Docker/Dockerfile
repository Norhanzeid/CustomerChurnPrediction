
# Use a minimal official Python 3.11 image as the base image
FROM python:3.11-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy all files from the current directory to the container's /app directory
COPY . .

# Install Python dependencies listed in requirements.txt, and avoid keeping cache to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 so the app can be accessed from outside the container
EXPOSE 8000

# Start the FastAPI app using Uvicorn, making it available on all network interfaces
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]

