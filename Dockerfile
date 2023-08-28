# Dockerfile
# Use the official Python 3.11.4 image as the base image
FROM python:3.11.4

# Install tesseract and its dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends libgl1-mesa-glx && \
    apt-get install -y --no-install-recommends tesseract-ocr && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt /app/

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt --default-timeout=2000

# Copy the Flask application code to the container
COPY app.py /app/
COPY modules /app/modules
# Expose the Flask app port
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
